# -*- coding: utf-8 -*-
from drf_client import configure as client_configure
import os

__author__ = '{{ cookiecutter.full_name }}'
__email__ = '{{ cookiecutter.email }}'
__version__ = '{{ cookiecutter.version }}'


def configure(filename="config.yaml", username=None, password=None, token=None):
    parent_dir = os.path.dirname(os.path.dirname(__file__))
    config_path = os.path.join(parent_dir, filename)
    client_configure(config_path, username=username,
                     password=password, token=token)
