from rest_framework import serializers

from collection.models import tag, user_state, user_entry


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = tag
        fields = '__all__'


class UserStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_state
        fields = '__all__'


class UserEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = user_entry
        fields = '__all__'
