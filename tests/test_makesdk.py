import os
import sys
import pytest
from drf_client_generator.management.commands import makesdk
from sampleapp.urls import router
from .helpers import make_temp_directory
from .fixtures import foos


class TestMakeResourceFile:

    def test_make_resources_generates_a_file_per_viewset(self):
        with make_temp_directory() as temp_dir:
            makesdk.make_resources(router=router, repo_path=temp_dir)
            expected_path = os.path.join(temp_dir, "foos.py")
            assert os.path.exists(expected_path)

        assert not os.path.exists(expected_path)

    def test_created_resource_file_is_importable(self):
        with make_temp_directory() as temp_dir:
            makesdk.make_resources(router=router, repo_path=temp_dir)
            sys.path.append(temp_dir)
            try:
                from foos import FooModel
            except ImportError:
                pytest.fail("Could not import generated model.")
