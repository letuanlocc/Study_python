from django.contrib import admin
from django.urls import path
from .views import CheckOutAPIView
from .views import WarehouseListAPI
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('', views.home,name = "home_page"),
    path('link/',views.link_view, name ="link_page"),
    path('menu/',views.menu_view,name ="menu_page"),
    path('milk/',views.milk_view, name = "milk_page"),
    path('register/',views.register, name = "register_page"),
    path('login/',views.login_view, name = "login_page"),
    path('logout/',views.logout_view, name = "logout_page"),
    path('api/checkouts/', CheckOutAPIView.as_view(), name='checkouts'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('search/', views.search, name='search_page'),
    path('warehouse/', views.Warehouse_view, name='warehouse_page'),
    path("upload/", views.upload_image, name="upload"),
    path('api/warehouse/',  WarehouseListAPI.as_view(), name='warehouse_api'),
    path('warehouse/warehouse_list/', views.warehosue_list, name='warehouse_list'),
    path("warehouse/warehouse_list/delete", views.delete_field, name="delete_field"), 
]
