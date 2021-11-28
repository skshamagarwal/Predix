from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Media(models.Model):
    mid = models.CharField(max_length=255, primary_key=True)    # Media ID
    title = models.CharField(max_length=255, null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    ranking = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)  # anime, movie, manga, tvseries
    genre = models.JSONField()  # List of genre [asa, asas, asas]
    rdate = models.CharField(max_length=50, null=True, blank=True) # YYYY-MM-DD
    year = models.CharField(max_length=4, null=True, blank=True)
    language = models.JSONField(null=True, blank=True)  # List of languages [japanese, english, hindi]
    cover = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    trailer = models.CharField(max_length=255, null=True, blank=True)
    released = models.BooleanField(default=True)
    objects = models.Manager()
    
    def __str__(self) -> str:
        return self.title  