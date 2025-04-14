from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView
from django.urls import re_path
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    re_path("register", RegisterView.as_view(), name="rest_register"),
    re_path("login", LoginView.as_view(), name="rest_login"),
    re_path("logout", LogoutView.as_view(), name="rest_logout"),
    re_path("user", UserDetailsView.as_view(), name="rest_user_details"),
    re_path("token/verify", TokenVerifyView.as_view(), name="token_verify"),
    re_path("token/refresh", get_refresh_view().as_view(), name="token_refresh"),
]
