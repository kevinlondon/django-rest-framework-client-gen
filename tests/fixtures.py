import pytest
import sys
from drf_client_generator.management.commands import makesdk
from sampleapp.urls import router
from .helpers import make_temp_directory


@pytest.fixture(scope="class")
def test_resources():
    """Returns an imported and generated instance of the `foo` test models."""
    with make_temp_directory() as temp_dir:
        makesdk.make_resources(router=router, repo_path=temp_dir)
        sys.path.append(temp_dir)
        import test_resources
        return test_resources
