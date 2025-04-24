from rest_framework import serializers

from .models import Category, MenuItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class MenuItemSerializer(serializers.ModelSerializer):
    # Explicitly define the price field only to override string coercion
    price = serializers.DecimalField(
        max_digits=10, decimal_places=2, coerce_to_string=False
    )

    category_name = serializers.CharField(source="category.name", read_only=True)
    is_favorite = serializers.SerializerMethodField()

    class Meta:
        model = MenuItem
        fields = "__all__"

    def get_is_favorite(self, obj):
        """Check if the menu item is favorited by the current user."""
        user = self.context["request"].user
        if user.is_authenticated:
            return user.favorites.filter(menu_item=obj).exists()
        return False
