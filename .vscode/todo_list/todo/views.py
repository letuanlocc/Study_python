from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Todo
from .serializer import TodoSerializer
#view de dang ki
from rest_framework import generics
from django.contrib.auth.models import User
from .serializer import RegisterSerializer


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]  
    
    def get_queryset(self):
        print(">>> Current user:", self.request.user) 
        return Todo.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
class TodoFilterViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.filter(completed=True).order_by('-created_at') #loc theo completed va created at tawng dan
    serializer_class = TodoSerializer
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()  
    serializer_class = RegisterSerializer
    
    
