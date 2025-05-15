from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),      # ví dụ
    path('signup/', views.signup_view, name='signup'),  
    path('logout/', views.signup_view, name='logout'),  
    # ví dụ
]