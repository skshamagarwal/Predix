from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Media(models.Model):
    id = models.AutoField(primary_key=True)
    mid = models.CharField(max_length=255)
    title = models.CharField(max_length=255, null=True, blank=True)
    rating = models.CharField(max_length=5, null=True, blank=True)
    ranking = models.CharField(max_length=5, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    genre = models.JSONField(null=True, blank=True)
    rdate = models.CharField(max_length=50, null=True, blank=True)
    year = models.CharField(max_length=4, null=True, blank=True)
    language = models.JSONField(null=True, blank=True)
    cover = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    trailer = models.CharField(max_length=255, null=True, blank=True)
    released = models.CharField(max_length=6, null=True, blank=True)
    objects = models.Manager()
    
    def __str__(self) -> str:
        return self.title  