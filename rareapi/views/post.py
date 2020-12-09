from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.response import Response
from rest_framework import viewsets
from rareapi.models import Post
from rareapi.serializers.postSerializer import PostListSerializer, PostSerializer

class PostViewSet(viewsets.ModelViewSet):

    def list(self, request):
        posts = Post.objects.all()

        category = self.request.query_params.get('type', None)
        if category is not None:
            posts = posts.filter(category__id=category)

        serializer = PostListSerializer(
            posts, many=True, context={'request': request})
        return Response(serializer.data)
        