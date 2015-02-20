from mock import patch
from drf_client import resources
from .fixtures import test_resources  # noqa


class TestTemplateGeneratedResources:

    def test_created_resource_file_contains_fields(self, test_resources):
        declared_fields = test_resources.FooModel._declared_fields
        expected_fields = "email", "content", "created"
        for fieldname, fieldtype in declared_fields.iteritems():
            assert fieldname in expected_fields
            assert isinstance(fieldtype, resources.Field)
