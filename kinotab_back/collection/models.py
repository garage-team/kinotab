from django.db import models

from movie.models import movie
from django.conf import settings


class tag(models.Model):
    name = models.CharField(max_length=256)


class user_state(models.Model):
    watched = models.BooleanField()
    score = models.IntegerField(null=True, blank=True)


class user_entry(models.Model):
    movie = models.ForeignKey(movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    tags = models.ManyToManyField(tag)
    state = models.ForeignKey(user_state, on_delete=models.CASCADE)
