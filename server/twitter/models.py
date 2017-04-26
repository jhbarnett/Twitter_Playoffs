from django.db import models


class Tweets(models.Model):
    user = models.TextField()
    user_url = models.URLField()
    user_image = models.URLField()
    text = models.TextField()
    created_at = models.DateTimeField()
    retweet_count = models.IntegerField()
    favorites_count = models.IntegerField()