from django_filters import rest_framework as filters

from .models import MenuItem


class MenuItemFilter(filters.FilterSet):
    is_favorite = filters.BooleanFilter(method="filter_is_favorite")

    class Meta:
        model = MenuItem
        fields = ["category", "is_available"]  # Keep existing filterable fields

    def filter_is_favorite(self, queryset, name, value):
        """
        Filter menu items based on whether they are favorited by the current user.
        """
        # Ensure request is available in the filter context (DRF usually provides this)
        if not hasattr(self, "request"):
            return queryset  # Cannot filter without request context

        user = self.request.user
        if value and user.is_authenticated:
            # Get IDs of menu items favorited by the user
            favorite_menu_item_ids = user.favorites.values_list(
                "menu_item_id", flat=True
            )
            # Filter the queryset
            return queryset.filter(id__in=favorite_menu_item_ids)
        # If value is False or user is not authenticated, return the original queryset
        # (or implement logic for explicitly filtering *non*-favorites if needed)
        return queryset
