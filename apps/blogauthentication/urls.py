from django.urls import path
from . import views

urlpatterns = [
    path("v1/register/", views.RegisterAPI.as_view(), name="register_api"),
    path("v1/login/", views.LoginAPI.as_view(), name="login_api"),
    path("v1/me/", views.UserAPI.as_view(), name="get_profile_api"),
]
