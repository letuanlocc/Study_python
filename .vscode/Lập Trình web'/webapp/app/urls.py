from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('link/',views.link_view, name ="link_page"),
    path('menu/',views.menu_view,name ="menu_page"),
    path('milk/',views.milk_view, name = "milk_page"),
]
