from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Blog cms API",
        default_version="v1",
        description="This api allows you to post to other sites and also to connect with your site",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="emmanuelthedeveloper@gmail.com"),
        license=openapi.License(name="BSD License"),
        #   url="http://localhost:8000/"
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("apps.blogauthentication.urls")),
    path("blog/", include("apps.blogs.urls")),
    # path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
]
