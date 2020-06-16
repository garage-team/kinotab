from rest_framework import serializers

from collection.models import tag, user_entry, item


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = tag
        fields = '__all__'


class UserEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = user_entry
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = item
        fields = '__all__'
