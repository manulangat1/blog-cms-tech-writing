from apps.blogs.exceptions import PostNotFound
from .models import Post


def get_post(id):
    try:
        post = Post.objects.get(id=id)
        return post
    except Post.DoesNotExist:
        raise PostNotFound
