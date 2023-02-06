from rest_framework import serializers
from rest_framework.fields import empty


class NovadataModelSerializer(serializers.ModelSerializer):
    representation_fields: list = []

    def to_representation(self, instance):
        if instance and not isinstance(instance, list):
            default_return = super(
                NovadataModelSerializer, self
            ).to_representation(instance)

            if self.representation_fields:
                for field_name, serializer in self.representation_fields:
                    default_return[field_name] = serializer(
                        getattr(instance, field_name)
                    ).data

            return default_return

    def __init__(self, instance=None, data=empty, **kwargs):
        super(NovadataModelSerializer, self).__init__(instance, data, **kwargs)
        self.to_representation(instance)
