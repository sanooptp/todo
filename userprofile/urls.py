from django.urls import path, include
from . import views

urlpatterns = [
    path('create_user/', views.AddUser.as_view(), name= 'create_user'),
]