from rest_framework import serializers

from menu.models import MenuItem
from menu.serializers import MenuItemSerializer

from .models import FavoriteDish


class FavoriteDishSerializer(serializers.ModelSerializer):
    # For displaying nested menu item details (read-only)
    menu_item = MenuItemSerializer(read_only=True)
    # For accepting menu_item ID during creation (write-only)
    menu_item_id = serializers.PrimaryKeyRelatedField(
        queryset=MenuItem.objects.all(), source="menu_item", write_only=True
    )

    class Meta:
        model = FavoriteDish
        fields = [
            "id",
            "user",
            "menu_item",  # Used for reading (nested details)
            "menu_item_id",  # Used for writing (accepting ID)
            "created_at",
        ]  # Keep 'user' here for reading
        read_only_fields = [
            "id",
            "user",
            "created_at",
            "menu_item",  # Keep the nested representation read-only
        ]  # Add 'user' to read_only_fields
