from rest_framework.exceptions import APIException


class PostNotFound(APIException):
    default_code = 404
    default_detail = "Post not found"
