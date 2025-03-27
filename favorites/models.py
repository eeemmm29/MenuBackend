from django.contrib.auth.models import User
from django.db import models

from menu.models import MenuItem


class FavoriteDish(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites")
    menu_item = models.ForeignKey(
        MenuItem, on_delete=models.CASCADE, related_name="favorited_by"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["user", "menu_item"]
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user.username}'s favorite: {self.menu_item.name}"
