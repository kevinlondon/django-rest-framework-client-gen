import os
from jinja2 import Environment, PackageLoader
from cookiecutter.prompt import prompt_for_config

PARENT_FOLDER = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
COOKIECUTTERS = os.path.join(PARENT_FOLDER, "cookiecutters")


def prep_environment():
    return Environment(
        loader=PackageLoader("drf_client_generator", "templates"),
        trim_blocks=True, lstrip_blocks=True
    )


def prompt_for_name():
    package_key = "Client SDK Name"
    ctx = prompt_for_config(context={
        "cookiecutter": {package_key: "boilerplate_sdk"}
    })
    return ctx[package_key]


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
