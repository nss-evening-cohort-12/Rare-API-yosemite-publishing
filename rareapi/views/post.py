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
    # filter_backends = (filters.DjangoFilterBackend)
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

    # def list(self, request):

    #     posts = Post.objects.all()

    #     category = self.request.query_params.get('category')
    #     if category is not None:
    #         posts = posts.filter(category__id=category)
    #         return posts

    #     serializer = PostListSerializer(posts, many=True, context={'request': request})
    #     return Response(serializer.data)



# In list
# / game_type = self.request.query_params.get('type', None)
#        if game_type is not None:
#           games = games.filter(gametype__id=game_type)
