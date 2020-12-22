from rest_framework import serializers
from rareapi.models import RareUser
# from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = RareUser
        fields = ('id', 'user')
        depth = 2
