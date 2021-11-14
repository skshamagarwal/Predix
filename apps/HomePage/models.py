from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Media(models.Model):
    mid = models.CharField(max_length=255, primary_key=True)    # Media ID
    title = models.CharField(max_length=255, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    type = models.IntegerField()  # Anime:0 or Movie:1 or Tv Series:2
    genre = models.JSONField()  # List of genre [asa, asas, asas]
    rdate = models.DateField(null=True, blank=True) # YYYY-MM-DD
    language = models.JSONField(null=True, blank=True)  # List of languages [japanese, english, hindi]
    cover = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    # sequal = models.CharField(max_length=255, null=True, blank=True)
    trailer = models.CharField(max_length=255, null=True, blank=True)
    objects = models.Manager()
    
    # def __str__(self) -> str:
    #     return self.title  
    
    
class Queries(models.Model):
    qid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    uid = models.ForeignKey(User, on_delete=CASCADE, null=True, blank=True)
    
    # def __str__(self) -> str:
    #     return "Query from " + str(self.name)
