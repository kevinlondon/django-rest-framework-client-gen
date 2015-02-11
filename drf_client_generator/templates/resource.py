from drf_client import resources, fields, utils


def get(*args, **kwargs):
    print "Getting {{ resource_name }}s."
    utils.get()


def create(*args, **kwargs):
    print "POSTing {{ resource_name }}s."
    utils.create()


class {{ resource_class }}(resources.Resource):
    {% for field, fieldtype in fields.iteritems() %}
    {{ field }} = fields.Field()
    {% endfor %}
