from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from userprofile.serializer import UserRegisterSerializer


class AddUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer