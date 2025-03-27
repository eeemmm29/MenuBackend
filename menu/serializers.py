from rest_framework import serializers

from .models import Category, FavoriteDish, MenuItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"


class FavoriteDishSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteDish
        fields = "__all__"
