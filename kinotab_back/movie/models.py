from django.db import models


class meta_field(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class meta_data(models.Model):
    meta_field = models.ForeignKey(meta_field, on_delete=models.CASCADE)
    value = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.meta_field


class item_type(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
