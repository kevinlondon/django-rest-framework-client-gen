from drf_client import resources, fields
import json

RESOURCE_PATH =  "{{ resource_path }}"


def create(resource=None, *args, **kwargs):
    print("POSTing {{ resource_name }}s.")
    resources.create(path=RESOURCE_PATH, model={{ resource_class }},
                     *args, **kwargs)


def get(resource=None, *args, **kwargs):
    print("Getting {{ resource_name }}s.")
    response = resources.get(path=RESOURCE_PATH, resource=resource,
                             *args, **kwargs)
    return resources.parse(response, model={{ resource_class}})


def update(resource=None, *args, **kwargs):
    print("Updating {{ resource_name }}s")
    resources.update(RESOURCE_PATH, resource=resource, *args, **kwargs)


def delete(resource=None, *args, **kwargs):
    print("Deleting {{ resource_name }}s")
    resources.delete(RESOURCE_PATH, resource=resource, *args, **kwargs)


class {{ resource_class }}(resources.Resource):
    {% for field, fieldtype in fields.iteritems() %}
    {{ field }} = fields.Field()
    {% endfor %}
