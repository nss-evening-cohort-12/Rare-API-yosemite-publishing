from rest_framework import viewsets
from rareapi.models import Subscription
from rareapi.serializers.subscription import SubscriptionSerializer

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
