from .models import ApUser
from rest_framework import routers, serializers, viewsets

class UserSerializer(serializers.HyperlinkedModelSerializer):
    fields = ApUser
    models = ['user', 'twitter_access_token', 'twitter_access_secret']