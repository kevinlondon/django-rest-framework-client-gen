from django.conf.urls import url, include
from .models import FooViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'foos', FooViewSet, base_name="foo")


urlpatterns = [
    url(r'^', include(router.urls)),
]
