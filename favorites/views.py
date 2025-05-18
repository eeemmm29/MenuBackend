from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import FavoriteDish
from .serializers import FavoriteDishSerializer

# Create your views here.


class FavoriteViewSet(viewsets.ModelViewSet):
    serializer_class = FavoriteDishSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FavoriteDish.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        """
        Deletes a favorite entry based on the menu item ID provided in the URL
        for the logged-in user.
        """
        user = request.user
        # The 'pk' from the URL is now treated as the menu_item_id
        menu_item_id = self.kwargs.get("pk")
        favorite_dish = get_object_or_404(
            FavoriteDish, user=user, menu_item_id=menu_item_id
        )
        self.perform_destroy(favorite_dish)  # Use perform_destroy for standard hooks
        return Response(status=status.HTTP_204_NO_CONTENT)
