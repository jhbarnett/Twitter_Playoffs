from rest_framework import viewsets
from rest_framework.response import Response

from .models import Tweets
from .serializers import TweetsSerializer
from .api import send_request

class TweetsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tweets to be viewed.
    """
    serializer_class = TweetsSerializer
    def list(self, request, *args, **kwargs):
        if request.method == 'GET':
            r = send_request()
            tweets = r['statuses']
            data = list(map(lambda x: x['text'], tweets))
            return Response(data)
        else:
            print("no GET")
