from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import related

class Post(models.Model):
    title = models.CharField(max_length=75)
    content = models.CharField(max_length=150)
    category = models.ForeignKey("Category",
    on_delete=CASCADE,
    related_name="categories",
    related_query_name="category"
    )
    publication_date = models.TextField()
    header_img_url = models.TextField()