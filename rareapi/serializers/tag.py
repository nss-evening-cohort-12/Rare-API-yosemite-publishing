from rest_framework import serializers
from rareapi.models import Tag, Post

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'label')
