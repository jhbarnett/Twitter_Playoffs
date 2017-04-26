from .models import Tweets
from rest_framework import serializers


class TweetsSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', input_formats='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Tweets
        fields = ('user', 'user_url', 'user_image',
                  'text', 'created_at', 'retweet_count',
                  'favorites_count')
