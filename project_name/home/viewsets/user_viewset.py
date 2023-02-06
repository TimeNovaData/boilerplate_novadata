from django.contrib.auth.models import User
from home.serializers import UserSerializer

from .novadata_model_viewset import NovadataModelViewSet


class UserViewSet(NovadataModelViewSet):
    queryset = User.objects.all()

    serializer_class = UserSerializer

    search_fields = []
