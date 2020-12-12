from django.db import models
from django.db.models import CASCADE


class Comment(models.Model):
    post_id = models.ForeignKey("Post", on_delete=CASCADE, related_name="comments", related_query_name="comment")
    author_id = models.ForeignKey("RareUser", on_delete=CASCADE, related_name="comments", related_query_name="comment")
    content = models.TextField()
    subject = models.CharField(max_length=100)
    created_on = models.DateTimeField()

    class Meta:
        ordering = ['-created_on']
