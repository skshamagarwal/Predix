from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.db import models
from apps.HomePage.models import Media

# class User(AbstractUser):
#     username = None
#     email = models.EmailField(unique=True)
#     forget_password = models.CharField(max_length=100, null=True, blank=True)
#     last_login_time = models.DateTimeField(null=True, blank=True)
#     last_logout_time = models.DateTimeField(null=True, blank=True)
#     objects = UserManger()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

class MyMedia(models.Model):
    mid = models.ForeignKey(Media, on_delete=CASCADE)
    uid = models.ForeignKey(User, on_delete=CASCADE, null=True, blank=True)
    watched = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()