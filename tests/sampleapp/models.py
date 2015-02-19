from rest_framework import serializers


class FooModel(object):
    pass


class FooSerializer(serializers.Serializer):
    class Meta:
        model = FooModel

    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()


class FooViewSet(object):
    serializer_class = FooSerializer
