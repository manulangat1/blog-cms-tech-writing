import pprint
from wsgiref import headers
from django.shortcuts import render
from decouple import config
from rest_framework import permissions, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.blogs.apis import HashnodeAPI, MediumAPI

from apps.blogs.getters import get_post
import requests

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


class PublishAPI(APIView):
    def patch(self, request, id):

        post = get_post(id)
        serializer = PostDetailSerializer(post)
        data = {
            "title": "This is test article from my site, Nothing here!",
            "contentFormat": "html",
            "content": "<p>this content 1.</p><p> This is content 2.</p>",
            "tags": ["development", "design", "test", "medium api"],
            # "public" will publish to gibubfor putting draft use value "draft"
            "publishStatus": "draft",
        }
        token = config("MEDIUM_API_TOKEN ")
        userId = MediumAPI.get_userId(token)
        # print(post.title, post.content, post.tags)
        # res = MediumAPI.post_to_medium(userId, token, post)
        hashnode = HashnodeAPI.get_articles(config("HASHNODE_API_TOKEN "))
        print(hashnode[0]["title"])
        for hashnode_posts in hashnode:
            postExists = Post.objects.filter(title=hashnode_posts["title"])
            if len(postExists) > 0:
                print("pass")
                if postExists[0].isPublished == False:
                    res = MediumAPI.post_to_medium(userId, token, postExists[0])
                    postExists[0].isPublished = True
                    postExists[0].save()
                else:
                    print("pass")
                    pass
                # pass
            else:
                new_post = Post.objects.create(
                    user=request.user,
                    title=hashnode_posts["title"],
                    content=hashnode_posts["contentMarkdown"],
                    image=hashnode_posts["coverImage"],
                    slug=hashnode_posts["slug"],
                )
                res = MediumAPI.post_to_medium(userId, token, new_post)
                new_post.isPublished = True
                new_post.save()
        # print(hashnode)

        return Response(serializer.data, status=status.HTTP_200_OK)
