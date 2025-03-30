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
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, redirect
from .models import Warehouse
from django.db import transaction
import cloudinary.uploader
from django.views import View
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
        searched = request.POST.get("search", "").strip().lower()
        warehouse = Warehouse.objects.filter(nameproduct__icontains = searched).values("nameproduct","price").distinct()
        username = request.user.username if request.user.is_authenticated else "Guest"
        context = {
            "username" : username
        }
        if warehouse.exists():
            context.update({'result' : warehouse})
            print(context)
            return render(request, "app/search.html", context)
        else:
            messages.error(request,"San pham khong co trong gio hang !")  # Gửi thông báo lỗi
            return redirect("home_page")
    return render(request, "app/search.html")
def menu_view(request):
        warehouse = Warehouse.objects.all()
        username = request.user.username if request.user.is_authenticated else "Guest"
        context = {
            "username" : username,
            "result" : warehouse
        }
        return render(request, "app/menu.html", context)
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
def process_order(id_product, quantity):
    with transaction.atomic():  # Đảm bảo tính toàn vẹn dữ liệu
        warehouse = Warehouse.objects.select_for_update().get(id_product=id_product)
        if warehouse.instock < quantity:
            return False
        else:
            warehouse.instock -= quantity
            warehouse.save()
            return True
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
            warehouse = Warehouse.objects.filter(nameproduct = nameproduct).first()
            id_product = warehouse.id_product
            quantity = item.get('quantity', 1)
            if not process_order(id_product,quantity):
                return Response({"message": "Không đủ hàng trong kho, hàng trong kho còn {} sản phẩm".format(warehouse.instock)}, status=status.HTTP_400_BAD_REQUEST)
            print("Đơn hàng thành công!")
        for item in cart:
            nameproduct = item.get('nameproduct')
            id_product = Warehouse.objects.filter(nameproduct = nameproduct).first()
            price = item.get('price', 0)
            user_id = int(request.session.get('_auth_user_id'))
            user_instance = User.objects.get(id=user_id)
            quantity = item.get('quantity', 1)
            checkout = Checkout.objects.create(
                id_product = id_product,
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
def is_staff(user):
    return user.is_staff
def is_admin_or_staff(user):
    return user.is_superuser or user.is_staff
@login_required
def Warehouse_view(request):
    print(f"User: {request.user}, Staff: {request.user.is_staff}, Superuser: {request.user.is_superuser}")
    if not is_admin_or_staff(request.user):
        messages.error(request,"Má không có đủ quyền để mà vô đây !")
        return redirect("home_page")
    warehouse_list = Warehouse.objects.all()
    context = {
        'warehouse' : warehouse_list,
        'is_superuser': request.user.is_superuser,
        'is_staff': request.user.is_staff,
    }
    return render(request, 'app/warehouse.html', context)
@csrf_exempt
def upload_image(request):
    if request.method == "POST":
        id_product = request.POST.get("id_product")
        nameproduct = request.POST.get("nameproduct")
        origin = request.POST.get("origin")
        price = request.POST.get("price")
        instock = request.POST.get("instock")
        image_file = request.FILES.get("image")

        if image_file:
            result = cloudinary.uploader.upload(image_file)
            image_url = result["secure_url"]
        else:
            image_url = None  # Không có ảnh

        Warehouse.objects.update_or_create(
            id_product=id_product,
            defaults={
                "nameproduct": nameproduct,
                "origin": origin,
                "price": price,
                "instock": instock,
                "image": image_url
            }
        )

        return JsonResponse({"message": "Sản phẩm đã được lưu!","image_url": image_url})

    return JsonResponse({"error": "Phương thức không hợp lệ!"}, status=400)
@login_required
def get_warehouse(request):
    if not is_admin_or_staff(request.user):
        messages.error(request,"Má không có đủ quyền để mà vô đây !")
        return redirect("home_page")
    warehouse = Warehouse.objects.values("id_product", "nameproduct", "origin", "price", "instock", "image")
    return render(request,'app/warehouse_list.html',{'warehouse' : warehouse})
    
def delete_field(request):
    print(request.POST)  # Xem thử có nhận được id_product không
    id_product = request.POST.get("id_product")
    warehouse= Warehouse.objects.filter(id_product=id_product)
    if warehouse.exists():
        warehouse.delete()
        messages.success(request,"DELETE SUCCESFULL")
    else:
        messages.error(request,"DELETE FAILURE")
    return redirect("warehouse_list")