from django.urls import path
from . import views
from knox.views import LogoutView

urlpatterns = [
    path("v1/posts/", views.PostAPI.as_view(), name="get_a_list_of_all_blogs"),
    path("v1/tags/", views.TagAPI.as_view(), name="get_all_tags"),
    path("v1/posts/<str:id>/", views.PostDetailAPI.as_view(), name="get_a_post_detail"),
    path("v1/post/<str:id>/publish", views.PublishAPI.as_view(), name="Publish")
    # path("v1/logout/", LogoutView.as_view(), name="logout_user"),
]
