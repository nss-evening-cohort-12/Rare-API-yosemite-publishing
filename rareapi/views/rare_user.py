from rest_framework import viewsets
from rareapi.models import RareUser

from rareapi.serializers.rare_user import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = RareUser.objects.all()
    serializer_class = UserSerializer
