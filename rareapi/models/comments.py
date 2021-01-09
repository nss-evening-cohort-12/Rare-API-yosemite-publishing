from django.db import models
from django.db.models import CASCADE


class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete=CASCADE, related_name="posts", related_query_name="posts", null = False, blank = True)
    author = models.ForeignKey("RareUser", on_delete=CASCADE, related_name="subscription_authors", related_query_name="subscription_author")
    content = models.TextField()
    subject = models.CharField(max_length=100)
    created_on = models.DateTimeField()

    class Meta:
        ordering = ['-created_on']
