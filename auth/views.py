from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)
    # authentication_classes = (JWTAuthentication,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class Login(APIView):
    def get_token_for_user(self, user):
        """
        :param user: user for which token is generated
        :return: {
            access_token: <value>
            refresh_token: <value>
        }
        """
        refresh = RefreshToken.for_user(user)

        return 'Bearer {} {}'.format(str(refresh.access_token), str(refresh))

    def post(self, request):
        data = request.data
        username = data.get('username', None)
        password = data.get('password', None)

        user = authenticate(username=username, password=password)

        request.user = user
        token = self.get_token_for_user(user)
        response = {'token': token}
        return Response({"data": response, "message": "success"}, status=status.HTTP_200_OK)
