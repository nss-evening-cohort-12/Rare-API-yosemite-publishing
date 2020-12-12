from rest_framework import viewsets
from rareapi.models import Comment
from rareapi.serializers import CommentSerializer, CreateCommentSerializer
from rest_framework.response import Response

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request):
        serializer = CreateCommentSerializer(data=request.data)
        if serializer.is_valid():
            comment = Comment.objects.create(**serializer.validated_data)
            serializer = CommentSerializer(comment)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HttpResponseBadRequest.status_code)
