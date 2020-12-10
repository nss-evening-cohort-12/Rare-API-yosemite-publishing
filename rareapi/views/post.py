from django.http.response import HttpResponseBadRequest
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.response import Response
from rest_framework import viewsets
from rareapi.models import Post
from rareapi.serializers.postSerializer import PostListSerializer, PostSerializer, PostCreateSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request):
        serializer = PostCreateSerializer(data=request.data)
        if serializer.is_valid():
            categories = serializer.validated_data.pop('categories')
            post = Post.objects.create(**serializer.validated_data)
            for category in categories:
                post.categories.add(category)

            serializer = PostListSerializer(post)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HttpResponseBadRequest.status_code)
        