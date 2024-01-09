from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Todo
from .serializers import TodoSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.db.models import Q


@api_view(['GET'])
def home(request):
    endpoints = ['/api/todos/', '/api/todos/?query=todo',
                 '/api/todo/1/', '/api/todo/1/delete',
                 '/api/todo/1/update/']
    return Response(endpoints)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def todos(request):
    queryset = None
    if request.method == 'GET':
        query = request.GET.get('query')
        if query is not None:
            search = ((Q(title=query) | Q(description__icontains=query))
                      & Q(user=request.user))
            queryset = Todo.objects.filter(search)
        else:
            queryset = Todo.objects.filter(user=request.user)

    elif request.method == 'POST':
        request_data = request.data
        serializer = TodoSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
    serializer = TodoSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def todo(request, pk):
    queryset = get_object_or_404(Todo.objects.filter(user=request.user), pk=pk)
    if request.method == 'GET':
        serializer = TodoSerializer(queryset)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TodoSerializer(queryset, request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_304_NOT_MODIFIED)

    elif request.method == 'DELETE':
        queryset.delete()
        return Response(data={'success': True},
                        status=status.HTTP_204_NO_CONTENT)
