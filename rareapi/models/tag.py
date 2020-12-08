from django.db import models
from django.db.models.deletion import CASCADE
from django.conf import settings
from django.db.models.expressions import Case
from django.db.models.fields import related

class Tag(models.Model):
    label = models.CharField(max_length=50)
