from rest_framework import viewsets
from rareapi.models import Comment
from rareapi.serializers import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
