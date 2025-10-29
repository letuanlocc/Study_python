from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet
from django.contrib import admin
router = DefaultRouter()
router.register(r'notes', NoteViewSet, basename='notes')
urlpatterns = [
    path('', include(router.urls)),
]