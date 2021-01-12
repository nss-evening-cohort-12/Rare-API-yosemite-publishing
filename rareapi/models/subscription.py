from django.db import models
from django.db.models.deletion import CASCADE
from django.conf import settings
from django.db.models.expressions import Case
from django.db.models.fields import related

class Subscription(models.Model):
    follower_id = models.ForeignKey("RareUser", related_name="subscriptions", related_query_name="subscription", on_delete=CASCADE)
    author_id  = models.ForeignKey("RareUser", on_delete=CASCADE, related_name="subscribers", related_query_name="subscriber")
