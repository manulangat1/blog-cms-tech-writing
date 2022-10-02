from django.shortcuts import render
from rest_framework import permissions, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.blogs.getters import get_post

# Create your views here.

from .models import Post, Tag
from .serializers import TagSerializer, PostDetailSerializer, PostSerializer


class TagAPI(generics.ListCreateAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all().order_by("-created_at")
    permission_classes = [permissions.IsAuthenticated]


class PostAPI(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by("-created_at")
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        data = self.request.data
        new_post = serializer.save(
            user=self.request.user, title=data["title"], content=data["content"]
        )
        all_posts = Post.objects.all().order_by("-created_at")
        serializer = PostSerializer(all_posts, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# class PostDetailAPI(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = PostDetailSerializer
#     queryset = Post.objects.all().order_by('-created_at')
#     lookup_field = ('id',)
#     permission_classes = (
#         permissions.IsAuthenticated,
#     )


class PostDetailAPI(APIView):
    def get(self, request, id):
        post = get_post(id)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
