from mock import patch
from drf_client import resources, api
from .fixtures import test_resources  # noqa


class TestTemplateGeneratedResources:

    def test_created_resource_file_contains_fields(self, test_resources):
        declared_fields = test_resources.FooModel._declared_fields
        expected_fields = "email", "content", "created"
        for fieldname, fieldtype in declared_fields.iteritems():
            assert fieldname in expected_fields
            assert isinstance(fieldtype, resources.Field)

    @patch.object(api, "get")
    def test_request_provides_the_cls_on_call(self, get_mock, test_resources):
        test_resources.get()
        get_mock.assert_called_with(cls=test_resources.FooModel)

    @patch.object(api, "create")
    def test_create_provides_the_cls_on_call(self, create_mock, test_resources):
        test_resources.create()
        create_mock.assert_called_with(cls=test_resources.FooModel)
