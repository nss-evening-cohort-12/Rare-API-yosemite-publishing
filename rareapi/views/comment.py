from rest_framework import viewsets
from rareapi.models import Comment as CommentModel
from rareapi.serializers import CommentSerializer, CreateCommentSerializer
from rest_framework.response import Response

class CommentViewSet(viewsets.ModelViewSet):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer

    def create(self, request):
        serializer = CreateCommentSerializer(data=request.data)
        if serializer.is_valid():
            comment = CommentModel.objects.create(**serializer.validated_data)
            serializer = CommentSerializer(comment)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HttpResponseBadRequest.status_code)

    
    def list(self, request):
        comments = CommentModel.objects.all()
        post = self.request.query_params.get('post', None)

        if post is not None:    
            comments = comments.filter(post__id=post)

        serializer = CommentSerializer(comments, many=True, context={'request': request})
        return Response(serializer.data)
