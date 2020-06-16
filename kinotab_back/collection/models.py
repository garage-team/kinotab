from django.db import models

from movie.models import item_type, meta_data
from django.conf import settings


class tag(models.Model):
    name = models.CharField(max_length=256)
    favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class item(models.Model):
    title = models.CharField(max_length=256)
    meta_data = models.ManyToManyField(meta_data)
    type = models.ForeignKey(item_type, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title


class user_entry(models.Model):
    item = models.ForeignKey(item, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    tags = models.ManyToManyField(tag)
    score = models.IntegerField()
    released = models.BooleanField(default=False)
