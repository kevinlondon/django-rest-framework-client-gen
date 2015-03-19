from django.core.management.base import BaseCommand
from django.conf import settings
from django.utils.importlib import import_module
from drf_client_generator import helpers


class Command(BaseCommand):
    help = "This command makes an SDK for you."

    def handle(self, *args, **options):
        package_name = helpers.get_package_name()
        repo_path = helpers.get_sdk_path(package_name)
        urls = import_module(settings.ROOT_URLCONF)
        helpers.make_resources(router=urls.router, repo_path=repo_path)
        return "Made you an SDK!"
