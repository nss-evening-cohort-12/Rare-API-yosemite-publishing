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
    # filter_backends = (filters.SearchFilter)

    # def create(self, request):
    #     # import pdb
    #     # pdb.set_trace()
    #     req_body = json.loads(request.body.decode())
    #     format, imgstr = request.data['header_img_url'].split(';base64,')
    #     ext = format.split('/')[-1]
    #     image_data = ContentFile(base64.b64decode(imgstr), name=f'{uuid.uuid4()}.{ext}')
        
    #     post = Post.objects.create(
    #         # ('id', 'user', 'title', 'content', 'category', 'publication_date', 'header_img_url', 'tags')
    #         user = req_body['user'],
    #         title = req_body['title'],
    #         content = req_body['content'],
    #         category = req_body['category'],
    #         publication_date = req_body['publication_date'],
    #         header_img_url = image_data
    #     )
    #     tags = req_body['tags']
    #     for tag in tags:
    #         post.tags.add(tag)
    #     post.save()
    #     serializer = PostListSerializer(post)
    #     return Response(serializer.data)
    #     # else:
    #     #     return Response(serializer.errors, HttpResponseBadRequest.status_code)
    def create(self, request):
            # Create a new post
            # import pdb
            # pdb.set_trace()
            rare_user = RareUser.objects.get(pk=request.data['user'])
            # Format post image
            format, imgstr = request.data['header_img_url'].split(';base64,')
            ext = format.split('/')[-1]

            image_data = ContentFile(base64.b64decode(imgstr), name=f'{uuid.uuid4()}.{ext}')
            # import pdb
            # pdb.set_trace()
            post = Post()
            post.title = request.data['title']
            post.publication_date = request.data['publication_date']
            post.header_img_url = image_data
            post.content = request.data['content']
            # post.approved = request.data['approved']
            post.user = rare_user
            category = Category.objects.get(pk=request.data['category'])
            post.category = category
            # tags = req.data['tags']
            # for tag in tags:
            #     post.tags.add(tag)
            try:
                post.save()
                post.tags.set(request.data["tags"])
                post.save()
                serializer = PostSerializer(post, context={'request': request})
                return Response(serializer.data)
            except ValidationError as ex:
                return Response({'reason': ex.message}, status=status.HTTP_400_BAD_REQUEST)
