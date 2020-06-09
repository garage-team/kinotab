from django.db import models


class meta_field(models.Model):
    name = models.CharField(max_length=256)


class meta_data(models.Model):
    meta_field = models.ForeignKey(meta_field, on_delete=models.CASCADE)
    value = models.CharField(max_length=256, null=True, blank=True)


class movie(models.Model):
    title = models.CharField(max_length=256)
    meta_data = models.ManyToManyField(meta_data)
