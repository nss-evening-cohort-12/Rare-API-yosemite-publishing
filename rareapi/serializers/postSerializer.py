from rest_framework import serializers
from rareapi.models import Post

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'category', 'publication_date', 'header_img_url')
        depth = 1