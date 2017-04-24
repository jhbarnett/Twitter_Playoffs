from django.db import models


class Tweets(models.Model):
    text = models.TextField()