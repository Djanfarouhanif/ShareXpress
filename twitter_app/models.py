from django.db import models
from django.contrib.auth import get_user_model




class ApiKeys(models.Model):
    api_keys = models.CharField(max_length=200)
    api_secrets = models.CharField(max_length=200)


class ApUser(models.Model):
    twitter_access_token = models.CharField(max_length=200)
    twitter_access_secret = models.CharField(max_length=200)
    twitter_image = models.ImageField(upload_to="twitter_image", default='', blank=True)
    def __str__(self):
        return self.user.username
