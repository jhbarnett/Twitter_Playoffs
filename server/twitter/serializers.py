from .models import Tweets
from rest_framework import serializers


class TweetsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tweets
        fields = ('url', 'text')
