from django.contrib import admin

from .models import FavoriteDish


@admin.register(FavoriteDish)
class FavoriteDishAdmin(admin.ModelAdmin):
    list_display = ("user", "menu_item", "created_at")
    list_filter = ("created_at",)
    search_fields = ("user__username", "menu_item__name")
