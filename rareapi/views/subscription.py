from rest_framework import viewsets
from rareapi.models import Subscription
from rareapi.serializers.subscription import SubscriptionSerializer
class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


    def get_queryset(self):
        author_id = self.request.query_params.get('author_id', None)
        follower_id = self.request.query_params.get('follower_id', None)
        if author_id and follower_id:
            print(author_id, follower_id)
            return self.queryset.filter(follower_id=follower_id).filter(author_id=author_id)
        else:
            return self.queryset
