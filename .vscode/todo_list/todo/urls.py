from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet
from .views import TodoFilterViewSet

router = DefaultRouter()
router.register(r'todos', TodoViewSet)
router.register(r'todos-filter', TodoFilterViewSet, basename='todo-filter')

urlpatterns = [
    path('', include(router.urls)),
]