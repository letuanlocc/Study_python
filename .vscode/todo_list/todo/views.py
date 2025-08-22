from django.shortcuts import render
from rest_framework import viewsets
from .models import Todo
from .serializer import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
class TodoFilterViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.filter(completed=True).order_by('-created_at') #loc theo completed va created at tawng dan
    serializer_class = TodoSerializer
    
    
    
