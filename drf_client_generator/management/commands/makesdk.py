from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.utils.importlib import import_module
from jinja2 import Environment, PackageLoader
from cookiecutter.main import cookiecutter
from cookiecutter.prompt import prompt_for_config
import os

from .updatesdk import update_resources

def prep_environment():
    env = Environment(loader=PackageLoader("drf_client_generator", "templates"),
                      trim_blocks=True, lstrip_blocks=True)
    return env


def get_template(template_name):
    env = prep_environment()
    return env.get_template(template_name)


def make_context(route, viewset, basename):
    serializer = viewset.serializer_class
    return {
        "repo_name": route,
        "resource_class": serializer.Meta.model.__name__,
        "name": basename,
        "fields": serializer().get_fields(),
        "route_name": route,
    }


def make_resources(router, repo_path):
    os.chdir(repo_path)
    for route, viewset, basename in router.registry:
        context = make_context(route, viewset, basename)
        url = "gh:kevinlondon/cookiecutter-drf-client-resource"
        cookiecutter(url, no_input=True, extra_context=context)

    update_resources(router, repo_path)


class Command(BaseCommand):
    help = "This command makes an SDK for you."

    def handle(self, *args, **options):
        url = "gh:kevinlondon/cookiecutter-drf-client"
        package_key = "SDK Package Name"
        ctx = prompt_for_config(context={"cookiecutter": {package_key: "boilerplate_sdk"}})
        package_name = ctx[package_key]
        cookiecutter(url, no_input=True, extra_context={"repo_name": package_name})
        repo_path = os.path.join(os.getcwd(), package_name, package_name)
        urls = import_module(settings.ROOT_URLCONF)
        make_resources(router=urls.router, repo_path=repo_path)
        return "Made you an SDK!"
