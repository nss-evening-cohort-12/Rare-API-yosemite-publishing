from django.db.models import query
from django.http import HttpResponseServerError
from django.views.generic.base import View
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rareapi.models import Tag
from rareapi.serializers import TagSerializer
class TagViewSet(ModelViewSet):
    
    queryset = Tag.objects.all()
    serializer_class=TagSerializer
