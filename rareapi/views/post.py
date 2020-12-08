from django.http.response import HttpResponseBadRequest
from rest_framework.response import Response
from rest_framework.serializers import ListSerializer
from rest_framework import viewsets
from rareapi.models import Post
from rareapi.serializers.postSerializer import PostListSerializer

class PostViewSet(viewsets.ModelViewSet):
    def list(self, request):
        """Handle GET requests to games resource
        Returns:
            Response -- JSON serialized list of games
        """
        posts = Post.objects.all()

        category = self.request.query_params.get('type', None)
        if category is not None:
            posts = posts.filter(category__id=category)

        serializer = PostListSerializer(
            posts, many=True, context={'request': request})
        return Response(serializer.data)