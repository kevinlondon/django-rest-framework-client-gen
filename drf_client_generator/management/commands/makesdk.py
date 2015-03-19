from django.core.management.base import BaseCommand
from drf_client_generator.helpers import prompt_for_name
from drf_client_generator.models import ClientSDK


class Command(BaseCommand):
    help = "This command makes an SDK for you."

    def handle(self, *args, **options):
        sdk_name = prompt_for_name()
        ClientSDK(sdk_name).make()
        return "Made you an SDK!"
