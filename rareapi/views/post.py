from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.response import Response
from rest_framework import viewsets
from rareapi.models import Post
from rareapi.serializers.postSerializer import PostListSerializer, PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
        