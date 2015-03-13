from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.utils.importlib import import_module
from jinja2 import Environment, PackageLoader
from cookiecutter.main import cookiecutter
from cookiecutter.prompt import prompt_for_config
import os


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


def update_resources(router, repo_path):
    os.chdir(repo_path)
    for route, viewset, basename in router.registry:
        context = make_context(route, viewset, basename)
        make_resource_file(context, repo_path)
        make_api_file(context, repo_path)
        print "Updated one resource."


def make_resource_file(context, repo_path):
    template = get_template("resources.py")
    folder = os.path.join(repo_path, context['repo_name'], "autogenerated")
    resources_path = os.path.join(folder, "resources.py")
    with open(resources_path, 'w') as fobj:
        fobj.write(template.render(**context))


def make_api_file(context, repo_path):
    template = get_template("api.py")
    folder = os.path.join(repo_path, context['repo_name'], "autogenerated")
    api_path = os.path.join(folder, "api.py")
    with open(api_path, 'w') as fobj:
        fobj.write(template.render(**context))


class Command(BaseCommand):
    help = "This command makes an SDK for you."

    def handle(self, *args, **options):
        package_key = "SDK Package Name"
        ctx = prompt_for_config(context={"cookiecutter": {package_key: "boilerplate_sdk"}})
        package_name = ctx[package_key]
        repo_path = os.path.join(os.getcwd(), package_name, package_name)
        urls = import_module(settings.ROOT_URLCONF)
        update_resources(router=urls.router, repo_path=repo_path)
        return "Updated you an SDK"
