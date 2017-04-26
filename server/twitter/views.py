from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import TweetsSerializer
from .api import fetch_tweets


class TweetsViewSet(viewsets.ViewSet):
    """
    API endpoint that allows tweets to be viewed.
    """
    def list(self, request):
        if request.method == 'GET':
            data = fetch_tweets("#NBAPlayoffs2017 OR #NBAPlayoffs")
            serializer = TweetsSerializer(data, many=True)

            return Response(serializer.data)
        else:
            print("no GET")
