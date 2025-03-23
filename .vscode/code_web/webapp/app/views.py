from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib import messages
from .forms import LoginForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .serializers import  CheckOutSerializer
from .models import Checkout
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
import requests
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication   
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
import json
from django.views.decorators.csrf import csrf_exempt
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
def search(request):
    if request.method == "POST":
        searched = request.POST.get("search", "")
        checkout = Checkout.objects.filter(nameproduct__contains = searched)
        if checkout.exists():
            return redirect("menu_page")
        else:
            messages.error(request, "Sản phẩm không có trong menu!")  # Gửi thông báo lỗi
            return redirect("home_page")
    return render(request, "app/search.html")
def menu_view(request):
    username = request.user.username if request.user.is_authenticated else "Guest"
    context = {"username": username}
    return render(request, 'app/menu.html',context) 
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect("login_page")  
        else:
             return render(request, 'app/register.html', {'form': form})
    else:
        form = RegisterForm()
    return render(request, 'app/register.html', {'form': form})
def login_view(request):
    if request.method == "POST":
        print("DEBUG: Form nhận request POST", request.POST)
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["user_name"]
            password = form.cleaned_data["pass_word"]
            user = authenticate(request, username=username, password=password,)
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
                    res.set_cookie("access_token", access_token, httponly=True, secure=True, max_age=3600, samesite="Lax")
                    return res
        else:
            print("DEBUG: Đăng nhập thất bại!") 
            messages.error(request, "Tên đăng nhập hoặc mật khẩu không đúng!")
    else:
        form = LoginForm()
    return render(request, "app/login.html", {"form": form})
def logout_view(request):
    logout(request)
    messages.success(request, "Bạn đã đăng xuất thành công!")
    return redirect("home_page")  
class CheckOutAPIView(APIView):  
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]   
    def get(self, request): 
        print(f"DEBUG: User: {request.user}, Authenticated: {request.user.is_authenticated}")  
        checkouts = Checkout.objects.all()  
        serializer = CheckOutSerializer(checkouts, many=True)  
        return Response(serializer.data)
    
    def post(self, request):  
        # cart_items = request.data.get('cartItems', [])
        cart = request.data.get('cart', [])
        print("Dữ liệu cart nhận được:", cart)
        for item in cart:
            nameproduct = item.get('nameproduct')
            price = item.get('price', 0)
            user_id = int(request.session.get('_auth_user_id'))
            user_instance = User.objects.get(id=user_id)
            quantity = item.get('quantity', 1)
            checkout = Checkout.objects.create(
                nameproduct= nameproduct, 
                price= price, 
                id_username=user_instance,
                username=user_instance.username,
                quantity = quantity 
            )
            print(f"Đã lưu sản phẩm: {nameproduct}, Giá: {price}, Số lượng: {quantity}")
            checkout.save()
        print("da luu vao databse")
        return Response({"message": "Thanh toán thành công!"}, status=status.HTTP_201_CREATED)
