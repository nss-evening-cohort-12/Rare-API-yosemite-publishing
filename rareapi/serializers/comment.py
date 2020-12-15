from rest_framework import serializers
from rareapi.models import Comment, Post
# from rareapi.serializers import PostSerializer

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'content', 'subject', 'created_on')
        depth = 2

class PostSerializer(serializers.ModelSerializer):
      class Meta:
        model = Post
        fields = ('id', 'user_id', 'title', 'content', 'category', 'publication_date', 'header_img_url')
        depth = 1

class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'post', 'author', 'content', 'subject', 'created_on')
