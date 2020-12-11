from rest_framework import serializers
from rareapi.models import Category, Post

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'label')

class PostSerializer(serializers.ModelSerializer):
      class Meta:
        model = Post
        fields = ('id', 'user_id', 'title', 'content', 'category', 'publication_date', 'header_img_url')
        depth = 1
