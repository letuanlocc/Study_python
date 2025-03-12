from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name = "home_page"),
    path('link/',views.link_view, name ="link_page"),
    path('menu/',views.menu_view,name ="menu_page"),
    path('milk/',views.milk_view, name = "milk_page"),
    path('register/',views.register_view, name = "register_page"),
    path('login/',views.login_view, name = "login_page"),
    path('logout/',views.logout_view, name = "logout_page"),
    path('check_out/',views.Check_out, name = "check_out_page"),
]
