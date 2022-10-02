from rest_framework import permissions, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from knox.models import AuthToken

from .serializers import LoginSerializer, RegisterSerilizer, UserSerializer
from django.contrib.auth import get_user_model

# Create your views here.


class RegisterAPI(generics.GenericAPIView):
    """

    This is an api that creates a new user
    (args)
            - email
            - firstname
            - lastname
            -password
    """

    serializer_class = RegisterSerilizer
    # parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "message": "User created successfully. Login to continue"
                # "user": UserSerilizer(user,context=self.get_serializer_context()).data,
                # "token":AuthToken.objects.create(user)[1]
            },
            status=status.HTTP_201_CREATED,
        )


class LoginAPI(generics.GenericAPIView):
    "This is an api that logs in a user"
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response(
            {
                # "message":"success"
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            },
            status=status.HTTP_200_OK,
        )


class UserAPI(generics.RetrieveUpdateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     print(instance)
    #     return Response({"Added successfully"})
