from django.db import models

from django.conf import settings


class Tag(models.Model):
    name = models.CharField(max_length=256)
    favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.name




class MetaField(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "meta_field"


class MetaData(models.Model):
    meta_field = models.ForeignKey(MetaField, on_delete=models.CASCADE)
    value = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.meta_field

    class Meta:
        db_table = "meta_data"


class ContentType(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "content_type"


class ContentItem(models.Model):
    title = models.CharField(max_length=256)
    meta_data = models.ManyToManyField(MetaData)
    type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "content_item"


class UserEntry(models.Model):
    item = models.ForeignKey(ContentItem, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    score = models.IntegerField()
    released = models.BooleanField(default=False)

    class Meta:
        db_table = "user_entry"
