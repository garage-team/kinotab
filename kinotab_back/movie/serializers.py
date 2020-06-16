from rest_framework import serializers

from movie.models import meta_field, meta_data, item_type


class MetaFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = meta_field
        fields = '__all__'


class MetaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = meta_data
        fields = '__all__'


class ItemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = item_type
        fields = '__all__'
