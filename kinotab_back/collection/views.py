from django.shortcuts import render

from rest_framework import viewsets, permissions

from collection.models import Tag, MetaField, MetaData, \
    ContentType, ContentItem, UserEntry
from collection.serializers import TagSerializer, ContentItemSerializer, UserEntrySerializer, \
    MetaFieldSerializer, MetaDataSerializer, ContentTypeSerializer


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    permission_classes = [permissions.AllowAny]


class ContentItemViewSet(viewsets.ModelViewSet):
    serializer_class = ContentItemSerializer
    queryset = ContentItem.objects.all()
    permission_classes = [permissions.AllowAny]


class UserEntryViewSet(viewsets.ModelViewSet):
    serializer_class = UserEntrySerializer
    queryset = UserEntry.objects.all()
    permission_classes = [permissions.AllowAny]


class MetaFieldViewSet(viewsets.ModelViewSet):
    serializer_class = MetaFieldSerializer
    queryset = MetaField.objects.all()
    permission_classes = [permissions.AllowAny]


class MetaDataViewSet(viewsets.ModelViewSet):
    serializer_class = MetaDataSerializer
    queryset = MetaData.objects.all()
    permission_classes = [permissions.AllowAny]


class ContentTypeViewSet(viewsets.ModelViewSet):
    serializer_class = ContentTypeSerializer
    queryset = ContentType.objects.all()
    permission_classes = [permissions.AllowAny]
