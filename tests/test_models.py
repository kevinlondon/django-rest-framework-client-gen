import os
from mock import Mock
import pytest
from rest_framework.routers import SimpleRouter
from drf_client_generator.models import ClientSDK


@pytest.fixture
def sdk():
    return ClientSDK(name="foo")


class TestSDK:

    def test_path_set_to_current_path_plus_name(self, sdk):
        assert sdk.path == os.path.join(os.getcwd(), sdk.name, sdk.name)

    def test_routers_dynamically_pulled_from_url_module(self, sdk):
        foo_router = SimpleRouter()
        baz_router = SimpleRouter()
        sdk._urls = Mock(foo_router=foo_router, baz_router=baz_router)
        assert foo_router in sdk.routers
        assert baz_router in sdk.routers

    def test_router_parsing_ignores_other_things(self, sdk):
        sdk._urls = Mock(thing=object(), thing2=object())
        assert not sdk.routers
