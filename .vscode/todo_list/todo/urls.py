from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet
from .views import TodoFilterViewSet
from .views import RegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router = DefaultRouter()
router.register(r'todos', TodoViewSet, basename='todos')
router.register(r'todos-filter', TodoFilterViewSet, basename='todo-filter')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # lo
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
]
