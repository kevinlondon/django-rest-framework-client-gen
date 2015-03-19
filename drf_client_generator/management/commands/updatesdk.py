from django.core.management.base import BaseCommand
from django.conf import settings
from django.utils.importlib import import_module
from drf_client_generator.helpers import prompt_for_name
from drf_client_generator.models import ClientSDK


class Command(BaseCommand):
    help = "This command updates an SDK for you."

    def handle(self, *args, **options):
        sdk_name = prompt_for_name()
        ClientSDK(sdk_name).update()
        return "Updated you an SDK"
