from django.urls import path
from graphene_django.views import GraphQLView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from . import views
from .schema import schema

urlpatterns = [
    path('', views.home, name='home'),
    path('api/todos/', views.todos, name='todos'),
    path('api/todo/<str:pk>/', views.todo, name='todo'),
    path('api/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema))
]
