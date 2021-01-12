from django.db import models
from django.db.models.deletion import CASCADE
from django.conf import settings
from django.db.models.expressions import Case
from django.db.models.fields import related

class RareUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    bio = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='avatars', null=True)
    created_on = models.DateField()
    active = models.BooleanField()
