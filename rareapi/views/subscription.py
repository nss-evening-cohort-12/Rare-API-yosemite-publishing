from rest_framework import viewsets
from rareapi.models import RareUser
from rareapi.serializers.subscription import SubscriptionSerializer

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = RareUser.objects.all()
    serializer_class = SubscriptionSerializer
