from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializer import NoteSerializer
from .models import Note
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
class NoteViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NoteSerializer
    
    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        # Gắn user hiện tại vào note khi tạo mới
        serializer.save(user=self.request.user)
    
# Create your views here.
