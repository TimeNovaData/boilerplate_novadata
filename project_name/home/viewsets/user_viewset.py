from django.contrib.auth.models import User
from home.serializers import UserSerializer
from rest_framework import filters, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    serializer_class = UserSerializer

    permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter]

    authentication_classes = [TokenAuthentication]

    search_fields = []
