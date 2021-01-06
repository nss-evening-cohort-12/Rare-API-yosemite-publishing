from django.contrib.auth.models import User
from rest_framework import serializers
from rareapi.models import RareUser
# from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = RareUser
<<<<<<< HEAD
        fields = ('id', 'user', 'profile_image')
=======
        fields = ('id', 'user', 'bio', 'profile_image', 'created_on', 'active')
>>>>>>> main
        depth = 2
