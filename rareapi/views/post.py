from django.http.response import HttpResponseBadRequest
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.response import Response
from rest_framework import viewsets, filters
from rareapi.models import Post, Category, category, tag, RareUser
from rareapi.serializers.postSerializer import PostCreateSerializer, PostListSerializer, PostSerializer
from django.core.files.base import ContentFile
import base64
import uuid
import json

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_fields = ('category', 'category__id', 'user', 'user__id', 'tags__label' )

    def create(self, request):
            rare_user = RareUser.objects.get(pk=request.data['user'])
            format, imgstr = request.data['header_img_url'].split(';base64,')
            ext = format.split('/')[-1]
            image_data = ContentFile(base64.b64decode(imgstr), name=f'{uuid.uuid4()}.{ext}')
            post = Post()
            post.title = request.data['title']
            post.publication_date = request.data['publication_date']
            post.header_img_url = image_data
            post.content = request.data['content']
            post.user = rare_user
            category = Category.objects.get(pk=request.data['category'])
            post.category = category
            
            try:
                post.save()
                post.tags.set(request.data["tags"])
                post.save()
                serializer = PostSerializer(post, context={'request': request})
                return Response(serializer.data)
            except ValidationError as ex:
                return Response({'reason': ex.message}, status=status.HTTP_400_BAD_REQUEST)

            
    def update(self, request, pk=None):
            rare_user = RareUser.objects.get(pk=request.data['user'])
            # format, imgstr = request.data['header_img_url'].split(';base64,')
            # ext = format.split('/')[-1]
            # image_data = ContentFile(base64.b64decode(imgstr), name=f'{uuid.uuid4()}.{ext}')
            post = Post.objects.get(pk=pk)
            post.title = request.data['title']
            post.publication_date = request.data['publication_date']
            post.header_img_url = request.data['header_img_url']
            post.content = request.data['content']
            post.user = rare_user
            category = Category.objects.get(pk=request.data['category'])
            post.category = category
            
            try:
                post.save()
                post.tags.set(request.data["tags"])
                post.reactions.set(request.data['reactions'])
                post.save()
                serializer = PostSerializer(post, context={'request': request})
                return Response(serializer.data)
            except ValidationError as ex:
                return Response({'reason': ex.message}, status=status.HTTP_400_BAD_REQUEST)

