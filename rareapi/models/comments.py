from django.db import models
from django.db.models import CASCADE


class Comments(models.Model):
    post_id = models.ForeignKey("Posts", on_delete=CASCADE, related_name="comments", related_query_name="comment")
    author_id = models.ForeignKey("RareUsers", on_delete=CASCADE, related_name="comments", related_query_name="comment")
    content = models.TextField()
    subject = models.CharField(max_length=100)
    created_on = models.DateTimeField()
