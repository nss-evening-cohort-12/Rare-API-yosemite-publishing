from rest_framework import viewsets
from rareapi.models import Reactions
from rareapi.serializers import ReactionSerializer

class ReactionViewSet(viewsets.ModelViewSet):
    queryset = Reactions.objects.all()
    serializer_class = ReactionSerializer