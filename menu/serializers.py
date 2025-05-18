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
    # Accept image as a write-only field for upload
    image = serializers.ImageField(write_only=True, required=False)
    image_url = serializers.URLField(read_only=True)

    class Meta:
        model = MenuItem
        fields = "__all__"
        extra_kwargs = {"image": {"write_only": True}, "image_url": {"read_only": True}}

    def create(self, validated_data):
        validated_data.pop("image", None)  # Remove image before model creation
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop("image", None)  # Remove image before model update
        return super().update(instance, validated_data)

    def get_is_favorite(self, obj):
        """Check if the menu item is favorited by the current user."""
        user = self.context["request"].user
        if user.is_authenticated:
            return user.favorites.filter(menu_item=obj).exists()
        return False
