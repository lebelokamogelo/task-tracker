from django.contrib.auth import authenticate
from django.db import IntegrityError
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


@api_view(['POST'])
def create_account(request):
    try:
        User.objects.create_user(**request.data, is_staff=True)
        return Response({'success': True}, status=status.HTTP_201_CREATED)
    except IntegrityError as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(request, email=email, password=password)

    refresh = None
    if user:
        refresh = RefreshToken.for_user(user)

    if refresh:
        return Response({'success': True, "access": str(refresh.access_token),
                         "refresh": str(refresh)},
                        status=status.HTTP_202_ACCEPTED)
    else:
        return Response({'error': 'Invalid credentials'},
                        status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    token = RefreshToken(request.data.get('refresh_token'))
    token.blacklist()
    return Response({'success': True}, status=status.HTTP_200_OK)
