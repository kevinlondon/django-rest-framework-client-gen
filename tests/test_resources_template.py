from drf_client import resources
from .fixtures import foos


class TestResources:

    def test_created_resource_file_contains_fields(self, foos):
        declared_fields = foos.FooModel._declared_fields
        expected_fields = "email", "content", "created"
        for fieldname, fieldtype in declared_fields.iteritems():
            assert fieldname in expected_fields
            assert isinstance(fieldtype, resources.Field)

    def test_get_uses_the_correct_class(self):
        pass
