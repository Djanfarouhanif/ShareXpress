from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ApiKeys(models.Model):
    api_keys = models.CharField(max_length=200)
    api_secrets = models.CharField(max_length=200)


class ApUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    twitter_access_token = models.CharField(max_length=200)
    twitter_access_secret = models.CharField(max_length=200)

    def __str__():
        return self.user.username
