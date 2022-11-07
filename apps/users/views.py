from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response 
from rest_framework.permissions import (IsAuthenticated, AllowAny)
from rest_framework.authentication import TokenAuthentication
from rest_framework import status

from django.contrib.auth import authenticate
from .serializers import (UserSerializer, StatusSerializer) 
from .models import (User, Status) 

# Create your views here.
class ListUsers(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        if not serializer.is_valid:
            return Response({'error': '404 error'})
        return  Response({'users': serializer.data})

class LoginUser(APIView):
    def post(self, request:Request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)

        if user is not None:
            response = {
                "message": "Login Succesfull",
                "token": user.auth_token.key ,
            }
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(data={'message': 'Invalid email or password'})

class UserView(APIView):
    serializer_class = UserSerializer
    def get(self, request: Request):
        user = User.objects.get(id=1)
        serializer = self.serializer_class(instance=user, many=False)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

class SignUp(APIView):
    serializer_class = UserSerializer

    def post(self, request:Request):
        data = request.data
        serializer = self.serializer_class(data=data, many=False)

        if serializer.is_valid():
            serializer.save()

            response = {
                'message': 'User created succesfull',
                'data': serializer.data
            }

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StatusView(APIView):
    serializer_class = StatusSerializer

    def get(self, request: Request):
        all_status = Status.objects.all()
        serializer = self.serializer_class(all_status, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request):
        data = request.data

        serializer = self.serializer_class(data=data, many=False)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

