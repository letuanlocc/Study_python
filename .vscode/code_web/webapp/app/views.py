from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib import messages
from .forms import LoginForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CheckOutSerializer
from .models import Check_out
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
import requests

# from .models import Don_hang
# Create your views here.
def home(request):
    username = request.user.username if request.user.is_authenticated else "Guest"
    context = {"username": username}
    return render(request, "app/home.html", context)
def milk_view(request):
    return render(request, 'app/milk.html')
def link_view(request):
    return render(request, 'app/link.html')
def menu_view(request):
    return render(request, 'app/menu.html') 
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Lưu user vào Django Authentication
            return redirect("login_page")  # Chuyển hướng sau khi đăng ký thành công
    else:
        form = RegisterForm()
    
    return render(request, "app/register.html", {"form": form})
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["user_name"]
            password = form.cleaned_data["pass_word"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                token_url = "http://127.0.0.1:8000/api/token/"
                data = {"username": username, "password": password}
                response = requests.post(token_url, json=data)
                if response.status_code == 200:
                    tokens = response.json()
                    access_token = tokens["access"]
                    
                    # 🔥 Lưu token vào cookie
                    res = redirect("home_page")
                    res.set_cookie("access_token", access_token, httponly=True, secure=True, max_age=3600)
                    return res
        else:
            messages.error(request, "Tên đăng nhập hoặc mật khẩu không đúng!")
    else:
        form = LoginForm()

    return render(request, "app/login.html", {"form": form})
def logout_view(request):
    logout(request)
    messages.success(request, "Bạn đã đăng xuất thành công!")
    return redirect("home_page")  # Quay về trang chủ sau khi đăng xuất

class CheckOutAPIView(APIView): 
    permission_classes = [IsAuthenticated]    
    def get(self, request): 
        checkouts = Check_out.objects.all()  
        serializer = CheckOutSerializer(checkouts, many=True)  
        return Response(serializer.data)
    
    def post(self, request):  
        mydata = CheckOutSerializer(data=request.data, context={"request": request})
        if mydata.is_valid():  
            mydata.save()  
            return Response(mydata.data, status=status.HTTP_201_CREATED)
        return Response(mydata.errors, status=status.HTTP_400_BAD_REQUEST)