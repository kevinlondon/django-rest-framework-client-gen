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


def get_resource_template():
    env = prep_environment()
    return env.get_template("resources.py")


def make_resources(router, repo_path):
    template = get_resource_template()
    for path, viewset, basename in router.registry:
        serializer = viewset.serializer_class
        fpath = os.path.join(repo_path, "{path}.py".format(path=path))
        with open(fpath, 'w') as fobj:
            context = {
                "resource_class": serializer.Meta.model.__name__,
                "resource_name": basename,
                "fields": serializer().get_fields(),
                "resource_path": path,
            }
            fobj.write(template.render(**context))


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
