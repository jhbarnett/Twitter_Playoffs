from .models import Tweets
from rest_framework import serializers


class TweetsSerializer(serializers.Serializer):
    class Meta:
        model = Tweets
        fields = ('text')
