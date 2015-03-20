import os
import contextlib
import tempfile
import shutil
import sys
from drf_client_generator.models import ClientSDK


@contextlib.contextmanager
def make_sdk(router):
    # from http://stackoverflow.com/questions/13379742
    temp_dir = tempfile.mkdtemp()
    sdk = ClientSDK(name="foo")
    sdk.path = temp_dir
    sdk._make_resources(router)
    sys.path.append(temp_dir)
    yield temp_dir
    shutil.rmtree(temp_dir)
