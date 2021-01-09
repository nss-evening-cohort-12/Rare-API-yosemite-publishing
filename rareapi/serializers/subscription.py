from rest_framework import serializers
from rareapi.models import Subscription

class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = ('id', 'follower_id', 'author_id')
        depth = 2
