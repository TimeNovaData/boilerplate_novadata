from django.contrib.auth.models import User

from .novadata_model_serializer import NovadataModelSerializer


class UserSerializer(NovadataModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
