from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.response import Response
from rest_framework.serializers import ListSerializer
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

    def create(self, request):

        rare_user = User.objects.get(user=request.auth.user)

        post = Post()
        post.title = request.data["title"]
        post.maker = request.data["maker"]
        post.number_of_players = request.data["numberOfPlayers"]
        post.skill_level = request.data["skillLevel"]
        post.user = user

        category = category.objects.get(pk=request.data["categoryId"])
        post.category = category

        try:
            post.save()
            serializer = PostSerializer(post, context={'request': request})
            return Response(serializer.data)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)