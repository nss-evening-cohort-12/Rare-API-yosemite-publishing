from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.models import User

class AuthUserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields =('id', 'password', 'last_login', 'is_superuser', 'username', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined', 'first_name')
        depth = 1
