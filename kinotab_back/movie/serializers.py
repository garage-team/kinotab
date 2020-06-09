from rest_framework import serializers

from movie.models import meta_field, meta_data, movie


class MetaFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = meta_field
        fields = '__all__'


class MetaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = meta_data
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = movie
        fields = '__all__'
