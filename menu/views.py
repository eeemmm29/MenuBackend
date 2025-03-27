from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category, MenuItem, FavoriteDish
from .serializers import (
    CategorySerializer,
    MenuItemSerializer,
    UserSerializer,
    FavoriteDishSerializer,
)
from django.contrib.auth.models import User

# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]

    @action(detail=True, methods=["post"])
    def toggle_favorite(self, request, pk=None):
        menu_item = self.get_object()
        user = request.user

        if not user.is_authenticated:
            return Response(
                {"error": "Authentication required"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        favorite, created = FavoriteDish.objects.get_or_create(
            user=user, menu_item=menu_item
        )

        if not created:
            favorite.delete()
            return Response({"status": "removed from favorites"})

        return Response({"status": "added to favorites"})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=["get"])
    def favorites(self, request):
        if not request.user.is_authenticated:
            return Response(
                {"error": "Authentication required"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        favorites = FavoriteDish.objects.filter(user=request.user)
        serializer = FavoriteDishSerializer(favorites, many=True)
        return Response(serializer.data)
