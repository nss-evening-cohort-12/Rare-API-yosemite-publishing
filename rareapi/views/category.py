from rest_framework import viewsets
from rareapi.models import Category
from rareapi.serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
