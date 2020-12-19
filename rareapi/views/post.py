from django.http.response import HttpResponseBadRequest
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.response import Response
from rest_framework import viewsets, filters
from rareapi.models import Post, Category, category
from rareapi.serializers.postSerializer import PostCreateSerializer, PostListSerializer, PostSerializer
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_fields = ('category', 'category__id')

    def create(self, request):
        serializer = PostCreateSerializer(data=request.data)
        if serializer.is_valid():
            tags = serializer.validated_data.pop('tags')
            post = Post.objects.create(**serializer.validated_data)
            for tag in tags:
                post.tags.add(tag)

            serializer = PostListSerializer(post)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, HttpResponseBadRequest.status_code)

    def list(self, request):
        posts = Post.objects.all()
        user = self.request.query_params.get('user', None)

        if user is not None:    
            posts = posts.filter(user__id=user)

        serializer = PostSerializer(posts, many=True, context={'request': request})
        return Response(serializer.data)
