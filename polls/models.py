from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    viewer_name = models.CharField(max_length=50)
    movie_title = models.CharField(max_length=100)
    rating = models.IntegerField(max_length=5)
    review = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.movie_title
