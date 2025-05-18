from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets

from .models import Category, MenuItem
from .serializers import CategorySerializer, MenuItemSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticatedOrReadOnly()]


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category", "is_available"]

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticatedOrReadOnly()]

    def perform_create(self, serializer):
        request = self.request
        image = request.FILES.get("image")
        image_url = None
        if image:
            import cloudinary.uploader

            result = cloudinary.uploader.upload(image)
            image_url = result.get("secure_url")
        serializer.save(image_url=image_url)

    def perform_update(self, serializer):
        request = self.request
        image = request.FILES.get("image")
        image_url = serializer.instance.image_url
        if image:
            import cloudinary.uploader

            result = cloudinary.uploader.upload(image)
            image_url = result.get("secure_url")
        serializer.save(image_url=image_url)
