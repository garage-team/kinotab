from rest_framework import serializers

from collection.models import Tag, MetaField, MetaData, \
    ContentType, ContentItem, UserEntry


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class UserEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEntry
        fields = '__all__'


class ContentItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentItem
        fields = '__all__'


class MetaFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaField
        fields = '__all__'


class MetaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaData
        fields = '__all__'


class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = '__all__'
