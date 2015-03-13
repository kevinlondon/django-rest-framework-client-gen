from drf_client import api
from {{ route_name }}.resources import {{ resource_class }}


def create(*args, **kwargs):
    return api.create(cls={{ resource_class }}, *args, **kwargs)


def get(*args, **kwargs):
    return api.get(cls={{ resource_class }}, *args, **kwargs)
