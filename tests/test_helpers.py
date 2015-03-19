import os
import sys
import pytest
from drf_client_generator import helpers
from sampleapp.urls import router
from .helpers import make_temp_directory
from .fixtures import test_resources


class TestMakeResourceFile:

    def test_make_resources_generates_a_file_per_viewset(self):
        with make_temp_directory() as temp_dir:
            helpers.make_resources(router=router, repo_path=temp_dir)
            expected_path = os.path.join(temp_dir, "test_resources")
            assert os.path.isdir(expected_path)

        assert not os.path.exists(expected_path)

    def test_created_resource_file_is_importable(self):
        with make_temp_directory() as temp_dir:
            helpers.make_resources(router=router, repo_path=temp_dir)
            sys.path.append(temp_dir)
            try:
                from test_resources import FooModel
            except ImportError:
                pytest.fail("Could not import generated model.")
