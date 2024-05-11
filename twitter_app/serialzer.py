from .models import ApUser
from rest_framework import routers, serializers, viewsets

class UserSerializer(serializers.ModelSerializer):
    fields = ApUser
    models = ['user', 'twitter_access_token', 'twitter_access_secret']