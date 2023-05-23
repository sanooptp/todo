from datetime import datetime
from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Todo
from .serializer import TodoSerializer, TodoCreateSerializer


class TodoCreateView(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoCreateSerializer
    permission_classed = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user,created_time= datetime.now())


class TodoDeleteView(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classed = [permissions.IsAuthenticated]


class TodoUpdateView(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoCreateSerializer
    permission_classed = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(created_time=datetime.now())


class TodoListView(generics.ListAPIView):
    serializer_class = TodoSerializer
    permission_classed = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Todo.objects.filter(user=self.request.user)
        return queryset