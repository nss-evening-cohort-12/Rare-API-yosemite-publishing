from django.http.response import HttpResponseBadRequest
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.response import Response
from rest_framework import viewsets, filters
from rareapi.models import Post, Category, category, tag, RareUser, Subscription
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

   
    def get_queryset(self):
        user_id = self.request.query_params.get('user_id', None)
        follower = self.request.query_params.get('subscribed', None)
        if user_id:
          return self.queryset.filter(user_id=user_id)
        elif follower:
          subscriptions = Subscription.objects.filter(follower_id=follower)
          return self.queryset.filter(user_id__in=subscriptions.values("author_id"))
        else:
          return self.queryset

 # def get_queryset(self):
    #   user_id =self.request.body.query_params.get('user_id', None)
    #   follower = self.request.query_params.get('subscribed', None)
      # if user_id:
      #   return self.queryset.filter(user_id=user_id)
      # elif follower:
      #   subscriptions = Subscription.objects.filter(follower_id=follower)
      #   return self.queryset.filter(user_id__in=subscriptions.value("author_id"))
      # else:
      #   return self.queryset
