from home.models import Profile
from home.serializers import ProfileSerializer
from rest_framework import filters, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()

    serializer_class = ProfileSerializer

    permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter]

    authentication_classes = [TokenAuthentication]

    search_fields = []
