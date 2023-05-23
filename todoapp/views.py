from datetime import datetime
from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Todo
from .serializer import TodoSerializer, TodoCreateSerializer
from rest_framework.response import Response
from rest_framework import status


class TodoCreateView(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoCreateSerializer
    permission_classed = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user,created_time= datetime.now())

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        response_data = self.modify_response(serializer.data)
        return Response(response_data, status=status.HTTP_201_CREATED)

    def modify_response(self, data):
        modified_data = {
            'message': 'Item created successfully',
            'data': data,
        }
        return modified_data


class TodoDeleteView(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classed = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        response_data = self.modify_response()
        return Response(response_data)

    def modify_response(self):
        # Modify the response message as needed
        modified_message = 'Item deleted successfully'
        return {'message': modified_message}


class TodoUpdateView(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoCreateSerializer
    permission_classed = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(created_time=datetime.now())

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        response_data = self.modify_response(request.data)
        return Response(response_data)

    def modify_response(self, data):
        modified_data = {
            'message': 'Item updated successfully',
            "data": data
        }
        return modified_data


class TodoListView(generics.ListAPIView):
    serializer_class = TodoSerializer
    permission_classed = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Todo.objects.filter(user=self.request.user)
        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset.exists():
            return Response({'message': 'No items available'})
        serializer = self.get_serializer(queryset, many=True)
        modified_data = self.modify_response_data(serializer.data)
        return Response(modified_data)
    
    def modify_response_data(self, data):
        user = self.request.user.username
        
        modified_data =  {"status": "Success", "user": user, "data": data}
        return modified_data