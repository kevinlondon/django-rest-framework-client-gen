from django.conf.urls import url, include
from .models import FooViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'test_resources', FooViewSet, base_name="test_resource")


urlpatterns = [
    url(r'^', include(router.urls)),
]
