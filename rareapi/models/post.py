from django.db import models
from django.db.models.deletion import CASCADE
from django.conf import settings
from django.db.models.fields import related

class Post(models.Model):
    user = models.ForeignKey("RareUser", related_name="posts", on_delete=CASCADE, default=1)
    title = models.CharField(max_length=75)
    content = models.TextField()
    category = models.ForeignKey("Category",
    on_delete=CASCADE,
    related_name="posts",
    related_query_name="post",
    default=1
    )
    publication_date = models.TextField()
    header_img_url = models.ImageField(upload_to='headerimg', null=True)
    tags = models.ManyToManyField("Tag", related_name="posts", related_query_name="post")
    approved = models.BooleanField(default=False)
    reactions = models.ManyToManyField("Reactions", related_name="posts", related_query_name="post")
