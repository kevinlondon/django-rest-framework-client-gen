import os
from django.conf import settings
from django.utils.importlib import import_module
from cookiecutter.main import cookiecutter

from rest_framework.routers import SimpleRouter
from rest_framework import serializers
from drf_client import fields
from .helpers import get_template, change_directory

PARENT_FOLDER = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
COOKIECUTTERS = os.path.join(PARENT_FOLDER, "cookiecutters")
USER_PATH = os.getcwd()


class ClientSDK(object):

    def __init__(self, name):
        self.name = name
        self.path = os.path.join(USER_PATH, name, name)
        self._urls = None
        self._routers = []
        self._collections = []

    @property
    def routers(self):
        if not self._routers:
            self._populate_routers()

        return self._routers

    def _populate_routers(self):
        if not self._urls:
            self._urls = import_module(settings.ROOT_URLCONF)

        url_names = dir(self._urls)
        for name in url_names:
            potential_router = getattr(self._urls, name)
            if isinstance(potential_router, SimpleRouter):
                self._routers.append(potential_router)

    def make(self):
        self._make_skeleton()
        for router in self.routers:
            self._make_resources(router)

        self._make_readme()

    def update(self):
        for router in self.routers:
            self._update_resources(router)

    def _make_resources(self, router):
        for entry in router.registry:
            resource = Resource(router_entry=entry, sdk_path=self.path)
            resource.make()
            self._collections.append(resource.collection)

    def _update_resources(self, router):
        for entry in router.registry:
            resource = Resource(router_entry=entry, sdk_path=self.path)
            resource.autogenerate()

    def _make_skeleton(self):
        template = os.path.join(COOKIECUTTERS, "sdk")
        cookiecutter(template, extra_context={"repo_name": self.name})

    def _make_readme(self):
        template = get_template("readme.rst")
        path = os.path.join(USER_PATH, self.name, "README.rst")
        context = {"name": self.name, "collections": self._collections}
        login_help =  self._get_login_help()
        if login_help:
            context['login'] = login_help

        with open(path, 'w') as fobj:
            fobj.write(template.render(context))

    def _get_login_help(self):
        try:
            auth_classes = settings.REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES']
        except KeyError:
            return None

        if 'rest_framework.authentication.BasicAuthentication' in auth_classes:
            return 'username="admin", password="password"'
        elif 'rest_framework.authentication.TokenAuthentication' in auth_classes:
            return 'token="myoauthtoken"'


class Resource(object):

    def __init__(self, router_entry, sdk_path):
        self.context = self._make_context(router_entry)
        self._sdk_path = sdk_path
        self.collection = self.context['route_name']

    def make(self):
        self._make_skeleton()
        self.autogenerate()

    def autogenerate(self):
        self._write_template("resources.py")
        self._write_template("api.py")

    def _make_skeleton(self):
        with change_directory(self._sdk_path):
            template = os.path.join(COOKIECUTTERS, "resource")
            cookiecutter(template, no_input=True, extra_context=self.context)

    def _make_context(self, router_entry):
        route, viewset, basename = router_entry
        serializer = viewset.serializer_class
        new_fields = FieldMapper(serializer().fields).remap_all()
        return {
            "repo_name": route,
            "route_name": route,
            "resource_class": serializer.Meta.model.__name__,
            "name": basename,
            "fields": new_fields
        }

    def _write_template(self, template_name):
        template = get_template(template_name)
        path = os.path.join(self._sdk_path, self.context['route_name'],
                            "autogenerated", template_name)
        with open(path, 'w') as fobj:
            fobj.write(template.render(**self.context))


class FieldMapper(object):

    FIELD_MAP = {
        serializers.DateTimeField: fields.DateTimeField
    }

    def __init__(self, serializer_fields):
        self.serializer_fields = serializer_fields

    def remap_all(self):
        """Take a set of the fields from the serializer and convert them.

        Returns:
            A new dictionary with the remapped fields for the client SDK.
        """
        new_fields = {}
        for field_name, field_type in self.serializer_fields.iteritems():
            new_fields[field_name] = self.remap_field(field_type)

        return new_fields

    def remap_field(self, field_type):
        """Recreate the instance of the field as a client SDK field type."""
        field_class = field_type.__class__
        try:
            field_type = self.FIELD_MAP[field_class]
        except KeyError:
            field_type = fields.Field

        return field_type()
