from django.db import models


class Reactions(models.Model):
    emoji = models.TextField()
    label = models.CharField(max_length=20)
