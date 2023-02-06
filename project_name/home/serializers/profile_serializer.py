from home.models import Profile

from .novadata_model_serializer import NovadataModelSerializer


class ProfileSerializer(NovadataModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
