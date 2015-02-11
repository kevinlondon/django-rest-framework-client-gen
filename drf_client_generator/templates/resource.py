from drf_client import resources, fields


class {{ resourcename }}(resources.Resource):
    {% for field, fieldtype in fields.iteritems() %}
    {{ field }} = {{ fieldtype }}
    {% endfor %}
