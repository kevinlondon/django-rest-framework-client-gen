import os
import pytest
from sampleapp.urls import router
from .helpers import make_sdk


class TestMakeResourceFile:

    def test_folder_exists_for_resource(self):
        with make_sdk(router=router) as sdk_dir:
            expected_path = os.path.join(sdk_dir, "test_resources")
            assert os.path.isdir(expected_path)

    def test_created_resource_file_is_importable(self):
        with make_sdk(router=router):
            try:
                from test_resources import FooModel
            except ImportError:
                pytest.fail("Could not import generated model.")
