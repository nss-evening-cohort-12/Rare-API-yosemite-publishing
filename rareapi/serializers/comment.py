from rest_framework import serializers
from rareapi.models import Comment, Post
# from rareapi.serializers import PostSerializer

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'post_id', 'author_id', 'content', 'subject', 'created_on')

class PostSerializer(serializers.ModelSerializer):
      class Meta:
        model = Post
        fields = ('id', 'user_id', 'title', 'content', 'category', 'publication_date', 'header_img_url')
        depth = 1
