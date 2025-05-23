"""
URL configuration for MenuBackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from authentication.views import UserViewSet
from favorites.views import FavoriteViewSet
from menu.views import CategoryViewSet, MenuItemViewSet

router = DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"menu-items", MenuItemViewSet)
router.register(r"users", UserViewSet)
router.register(r"favorites", FavoriteViewSet, basename="favorite")


def hello_world(request):
    return HttpResponse("Hello, World!")


urlpatterns = [
    path("", hello_world, name="home"),
    path("auth/", include("authentication.urls")),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
]
