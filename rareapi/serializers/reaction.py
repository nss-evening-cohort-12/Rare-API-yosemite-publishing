from rest_framework import serializers
from rareapi.models import Reactions

class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reactions
        fields = ('id', 'emoji','label')