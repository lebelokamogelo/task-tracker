from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
import requests


@api_view(['POST'])
def create_account(request):
    try:
        user = User.objects.create_user(**request.data, is_staff=True)
        return Response({'success': True}, status=status.HTTP_201_CREATED)
    except IntegrityError as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)
    response = requests.post('http://localhost:8000/api/token/', json={'username': username, 'password': password})
    if user and response.status_code == 200:
        login(request, user)
        return Response({'success': True, "access": response.json()['access']}, status=status.HTTP_202_ACCEPTED)
    else:
        return Response({'error_message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    logout(request)
    return Response({'success': True}, status=status.HTTP_200_OK)