from rest_framework import viewsets
from .serializers import TweetsSerializer
from .models import Tweets


class TweetsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Tweets.objects.all()
    serializer_class = TweetsSerializer

