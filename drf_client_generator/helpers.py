import contextlib
import os
from jinja2 import Environment, PackageLoader
from cookiecutter.prompt import prompt_for_config


def prep_environment():
    return Environment(
        loader=PackageLoader("drf_client_generator", "templates"),
        trim_blocks=True, lstrip_blocks=True
    )


def prompt_for_name():
    package_key = "Client SDK Name"
    ctx = prompt_for_config(context={"cookiecutter": {package_key: "drf_sdk"}})
    return ctx[package_key]


def get_template(template_name):
    env = prep_environment()
    return env.get_template(template_name)


@contextlib.contextmanager
def change_directory(new_directory):
    original_directory = os.getcwd()
    os.chdir(new_directory)
    yield
    os.chdir(original_directory)
