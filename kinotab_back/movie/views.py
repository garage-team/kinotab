from django.shortcuts import render

from rest_framework import viewsets, permissions

from movie.models import meta_field, meta_data, item_type
from movie.serializers import MetaFieldSerializer, MetaDataSerializer, ItemTypeSerializer


class MetaFieldViewSet(viewsets.ModelViewSet):
    serializer_class = MetaFieldSerializer
    queryset = meta_field.objects.all()
    permission_classes = [permissions.AllowAny]


class MetaDataViewSet(viewsets.ModelViewSet):
    serializer_class = MetaDataSerializer
    queryset = meta_data.objects.all()
    permission_classes = [permissions.AllowAny]

class ItemTypeViewSet(viewsets.ModelViewSet):
    serializer_class = ItemTypeSerializer
    queryset = item_type.objects.all()
    permission_classes = [permissions.AllowAny]