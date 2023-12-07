from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.db import IntegrityError
from django.contrib.auth import authenticate, login


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
    if user:
        login(request, user)
        return Response({'success': True}, status=status.HTTP_202_ACCEPTED)
    else:
        return Response({'error_message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
