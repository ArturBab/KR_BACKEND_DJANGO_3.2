from django.shortcuts import render
from django.http import HttpResponse
from backend.serializers import *
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .permissions import IsAuthorUpdateOnly, IsAdmin
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
import jwt
import datetime


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class LoginAPIView(APIView):
    def post(self, request):
        name = request.data['name']
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('Данный пользователь не найден.')

        if not user.check_password(password):
            raise AuthenticationFailed('Некорректный пароль.')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret',
                           algorithm='HS256').decode('utf-8')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt-token': token,
            'message': 'успешно.'
        }

        return response


class UserAPIAuthView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Данный пользователь не авторизован.')

        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Данный пользователь не авторизован.')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)


class LogoutAPIView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'Вы вышли из системы.'
        }

        return response


class ArticleAPIListAndPost(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ArticleAPIUpdate(generics.RetrieveUpdateAPIView, generics.RetrieveDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthorUpdateOnly,)


class AuthorAPIPost(generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthenticated,)


class AuthorAPIAdmList(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthorUpdateOnly,)
# Create your views here.
