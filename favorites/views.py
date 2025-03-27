from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import FavoriteDish
from .serializers import FavoriteDishSerializer

# Create your views here.


class FavoriteViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteDishSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FavoriteDish.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
