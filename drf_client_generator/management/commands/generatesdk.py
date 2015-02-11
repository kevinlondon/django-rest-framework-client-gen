from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.utils.importlib import import_module
from cookiecutter.main import cookiecutter
import os


class Command(BaseCommand):
    args = '<package_name>'
    help = "This command makes an SDK for you."

    def handle(self, package_name, *args, **options):
        print package_name

        url = "gh:kevinlondon/cookiecutter-drf-client"
        cookiecutter(url, no_input=True, extra_context={"repo_name": package_name})
        repo_path = os.path.join(os.getcwd(), package_name, package_name)
        fpath = os.path.join(repo_path, "f.txt")

        urls = import_module(settings.ROOT_URLCONF)
        for path, viewset, basename in urls.router.registry:
            print "Looking at ", viewset
            serializer = viewset.serializer_class
            fpath = os.path.join(repo_path, "{0}.py".format(basename))
            with open(fpath, 'w') as fobj:
                #print serializer().get_fields()
                for fieldname, field in serializer().get_fields().iteritems():
                    fobj.write("{name}: {field}\n".format(name=fieldname, field=field))



        return "Made you an SDK!"
