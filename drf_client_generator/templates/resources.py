from drf_client import resources, fields, api
import json


class Auto{{ resource_class }}(resources.Resource):

    _route = "{{ route_name }}"

    {% for field, fieldtype in fields.iteritems() %}
    {{ field }} = fields.Field()
    {% endfor %}
