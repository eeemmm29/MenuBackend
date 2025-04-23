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

    class Meta:
        model = MenuItem
        fields = "__all__"
