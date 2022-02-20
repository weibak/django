from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profiles"
    )
    age = models.IntegerField()
    image = models.ImageField(blank=True, null=True)
    status = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)


class Tags(models.Model):
    user = models.CharField(max_length=100)
    profiles = models.ManyToManyField(Profile)
