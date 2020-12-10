from rest_framework import serializers
from rareapi.models import Post

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user_id', 'title', 'content', 'category', 'publication_date', 'header_img_url')
        depth = 1

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        url = serializers.HyperlinkedIdentityField(
            view_name='post',
            lookup_field='id'
        )
        fields = ('id', 'user_id', 'title', 'content', 'category', 'publication_date', 'header_img_url')
        depth = 1

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'user_id', 'title', 'content', 'category', 'publication_date', 'header_img_url')