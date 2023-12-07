from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.create_account, name='create'),
    path('login/', views.login_user, name='login'),
]