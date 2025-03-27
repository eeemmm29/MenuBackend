from rest_framework import serializers
from .models import FavoriteDish
from menu.serializers import MenuItemSerializer


class FavoriteDishSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer(read_only=True)

    class Meta:
        model = FavoriteDish
        fields = "__all__"
