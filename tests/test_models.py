import os
from mock import Mock
import pytest
from rest_framework.routers import SimpleRouter
from rest_framework import serializers

from drf_client import fields
from drf_client_generator.models import ClientSDK, Resource, FieldMapper
from sampleapp.urls import router
from sampleapp.models import FooSerializer


@pytest.fixture
def sdk():
    return ClientSDK(name="foo")


@pytest.fixture
def resource():
    resource = Resource(sdk_path="foo", router_entry=router.registry[0])
    return resource


@pytest.fixture
def field_mapper():
    return FieldMapper(serializer_fields=None)


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


class TestFieldMapping:

    def test_field_remapper_will_remap_all_fields(self):
        fields = FooSerializer().fields
        mapper = FieldMapper(serializer_fields=fields)
        remapped_fields = mapper.remap_all()
        for field_name in fields:
            assert field_name in remapped_fields

    def test_datetime_field_maps_to_dt_field(self, field_mapper):
        field = field_mapper.remap_field(serializers.DateTimeField())
        assert isinstance(field, fields.DateTimeField)

    def test_basic_field_maps_in_field_object(self, field_mapper):
        field = field_mapper.remap_field(serializers.EmailField())
        assert isinstance(field, fields.Field)
