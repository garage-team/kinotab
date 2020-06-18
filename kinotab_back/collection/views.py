from django.shortcuts import render

from rest_framework import viewsets, permissions

from collection.models import tag, item, user_entry
from collection.serializers import TagSerializer, ItemSerializer, UserEntrySerializer


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = tag.objects.all()
    permission_classes = [permissions.AllowAny]

class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = item.objects.all()
    permission_classes = [permissions.AllowAny]

class UserEntryViewSet(viewsets.ModelViewSet):
    serializer_class = UserEntrySerializer
    queryset = user_entry.objects.all()
    permission_classes = [permissions.AllowAny]