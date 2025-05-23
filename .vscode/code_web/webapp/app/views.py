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
from .serializers import CartItemSerializer
from .serializers import WarehouseSerializerList
from rest_framework.generics import ListAPIView
from .serializers import WarehouseSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework import generics
import logging
from collections import defaultdict
from django.db.models import Sum
# from .models import Don_hang
# Create your views here.

def home(request):
    username = request.user.username if request.user.is_authenticated else "Guest"
    print(f"DEBUG: User: {request.user.username}, Authenticated: {request.user.is_authenticated}")
    context = {"username": username}
    return render(request, "app/home.html", context)
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def manage_account(request):
    user = request.user
    
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        user.username = username
        user.email = email
        user.save()
        messages.success(request, "Thay đổi thông tin tài khoản thành công!")
        return redirect('manage_account_page')
    user_object = User.objects.filter(id=request.user.id).values('username', 'email').distinct()
    context = {
        "user_object": user_object
    }
    return render(request, "app/manage_account.html", context)

def milk_view(request):
    return render(request, 'app/milk.html')
def link_view(request):
    return render(request, 'app/link.html')
def is_staff(user):
    return user.is_staff
def is_admin_or_staff(user):
    return user.is_superuser or user.is_staff
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
        warehouse = Warehouse.objects.all().order_by('nameproduct')
        username = request.user.username if request.user.is_authenticated else "Guest"
        context = {
            "username" : username,
            "result" : warehouse
        }
        return render(request, "app/menu.html", context)
def purchased(request):
    username = request.user.username if request.user.is_authenticated else "Guest"
    total = None
    turnover = [] 
    product = []
    chart_labels_turnover = []
    chart_values_turnover = []
    chart_labels_product = []
    chart_values_product = []
    year = None
    #chart quantity product purchasedpurchased
    data = Checkout.objects.values("nameproduct","quantity")
    product = defaultdict(int)
    for item in data:
        product[item["nameproduct"]] += item["quantity"]
    chart_labels_product = [nameproduct for nameproduct, _ in product.items()]
    chart_values_product = [price for _, price in product.items()]
    #chart turnover
    if request.method == "POST":
        year = request.POST.get("year", "").strip()
        month = request.POST.get("month", "").strip()
        classify = request.POST.get("classify", "").strip()
        year = year
        month = month
        super_user = User.objects.filter(is_superuser = True).values_list("username",flat=True)
        normal_user = User.objects.filter(is_superuser = False).values_list("username",flat=True)
        super_user = list(super_user)  
        normal_user = list(normal_user) 
        print("classify:", classify)
        print("super_user:", super_user)
        print("normal_user:", normal_user) 
        if classify == "online":
            if year: # create chart for year
                data = Checkout.objects.filter(date_time__year=year).exclude(username__in=super_user).exclude(username="").values("price","nameproduct","date_time","quantity")
                total = sum(item["price"] * item["quantity"] for item in data)
                turnover = list(data)
                month_total = defaultdict(int)
                for item in data:
                    data_month = item["date_time"].month
                    month_total[data_month] += (item["price"] * item["quantity"])
                chart_labels_turnover = [month for month, _ in month_total.items()]
                chart_values_turnover = [value for _, value in month_total.items()]
            if month and year: # create chart for year and month
                data = Checkout.objects.filter(date_time__year=year, date_time__month=month).exclude(username__in=super_user).exclude(username="").values("price","nameproduct","date_time","quantity","username")
                print("data:", data)
                total = sum(item["price"] * item["quantity"]  for item in data)
                turnover = list(data)
                day_total = defaultdict(int)
                for item in data:
                    day = item["date_time"].day
                    day_total[day] += (item["price"] * item["quantity"])
                chart_labels_turnover = [day for day, _ in day_total.items()]
                chart_values_turnover = [value for _, value in day_total.items()]
        elif classify == "offline":
            if year: # create chart for year
                data = Checkout.objects.filter(date_time__year=year).exclude(username__in=normal_user).exclude(username="").values("price","nameproduct","date_time","quantity")
                total = sum(item["price"] * item["quantity"] for item in data)
                turnover = list(data)
                month_total = defaultdict(int)
                for item in data:
                    data_month = item["date_time"].month
                    month_total[data_month] += (item["price"] * item["quantity"])
                chart_labels_turnover = [month for month, _ in month_total.items()]
                chart_values_turnover = [value for _, value in month_total.items()]
            if month and year: # create chart for year and month
                data = Checkout.objects.filter(date_time__year=year, date_time__month=month).exclude(username__in=normal_user).exclude(username="").values("price","nameproduct","date_time","quantity","username") 
                print("data:", data)
                total = sum(item["price"] * item["quantity"]  for item in data)
                turnover = list(data)
                day_total = defaultdict(int)
                for item in data:
                    day = item["date_time"].day
                    day_total[day] += (item["price"] * item["quantity"])
                chart_labels_turnover = [day for day, _ in day_total.items()]
                chart_values_turnover = [value for _, value in day_total.items()]
        else:
            if year: # create chart for year
                data = Checkout.objects.filter(date_time__year=year).exclude(username="").values("price","nameproduct","date_time","quantity")
                total = sum(item["price"] * item["quantity"] for item in data)
                turnover = list(data)
                month_total = defaultdict(int)
                for item in data:
                    data_month = item["date_time"].month
                    month_total[data_month] += (item["price"] * item["quantity"])
                chart_labels_turnover = [month for month, _ in month_total.items()]
                chart_values_turnover = [value for _, value in month_total.items()]
            if month and year: # create chart for year and month
                data = Checkout.objects.filter(date_time__year=year, date_time__month=month).exclude(username="").values("price","nameproduct","date_time","quantity","username") 
                print("data:", data)
                total = sum(item["price"] * item["quantity"]  for item in data)
                turnover = list(data)
                day_total = defaultdict(int)
                for item in data:
                    day = item["date_time"].day
                    day_total[day] += (item["price"] * item["quantity"])
                chart_labels_turnover = [day for day, _ in day_total.items()]
                chart_values_turnover = [value for _, value in day_total.items()]
    context = {
        "username" : username,
        "total" : total,
        "result" : turnover,
        "chart_data": {
            "labels": json.dumps(chart_labels_turnover),
            "values": json.dumps(chart_values_turnover),
        },
        "chart_data_product": {
            "labels": json.dumps(chart_labels_product),
            "values": json.dumps(chart_values_product),
        },
    }
    return render(request, "app/purchased.html", context)
def process_order(id_product, quantity):
    with transaction.atomic():  
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
            username = request.user.username
            price = item.get('price')
            quantity = item.get('quantity', 1)
            if not process_order(id_product,quantity):
                return Response({"message": "Không đủ hàng trong kho, hàng trong kho còn {} sản phẩm".format(warehouse.instock)}, status=status.HTTP_400_BAD_REQUEST)
            print("Đơn hàng thành công!")
            data = {
            'id_product': id_product,
            'username': username,
            'nameproduct': nameproduct,
            'price': price,
            'quantity': quantity,
            'id_username': request.user.id  
            }
            order_success = []
            serializer = CheckOutSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                print(f"Đã lưu sản phẩm: {nameproduct}, Giá: {price}, Số lượng: {quantity}, username: {username}")
                print("da luu vao databse")
                order_success.append(nameproduct)
            else:
                return Response({"message": "Thanh toán thất bại!"}, status=status.HTTP_400_BAD_REQUEST)
        if order_success:
            return Response({"message": "Thanh toán thành công!"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Không có sản phẩm nào được thanh toán!"}, status=status.HTTP_400_BAD_REQUEST)
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
class WarehouseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer 
    permission_classes = [IsAdminUser] 
    authentication_classes = [SessionAuthentication] 
    lookup_field = 'id_product'       
    lookup_url_kwarg = 'id_product'   
    def perform_update(self, serializer):
        print(f"DEBUG: Payload nhận được: {self.request.data}")
        print(f"DEBUG: FILES nhận được: {self.request.FILES}")
        instance = serializer.instance
        if not instance:
           print("DEBUG: Không tìm thấy đối tượng cần cập nhật.")
        image_file = self.request.FILES.get("image")
        image_url = instance.image  # Mặc định giữ URL ảnh cũ

        if image_file:
            try:
                # Xóa ảnh cũ trên Cloudinary nếu tồn tại
                if instance.image:
                    try:
                        public_id = instance.image.split('/')[-1].split('.')[0]
                        print(f"Đang xóa ảnh cũ trên Cloudinary: {public_id}")
                        cloudinary.uploader.destroy(public_id)
                    except Exception as delete_error:
                        print(f"Lỗi xóa ảnh cũ trên Cloudinary: {delete_error}")

                # Upload ảnh mới lên Cloudinary
                print(f"Đang tải ảnh mới lên Cloudinary: {image_file.name}")
                result = cloudinary.uploader.upload(
                    image_file,
                    folder="warehouse_images"
                )
                image_url = result.get("secure_url")  
                print(f"Tải ảnh mới thành công: {image_url}")
            except Exception as e:
                print(f"Lỗi tải ảnh mới lên Cloudinary: {e}")
                raise serializer.ValidationError({"image": f"Tải ảnh mới thất bại: {e}"})

        
        serializer.save(image=image_url)
        print(f"Đã cập nhật sản phẩm: {instance.id_product}")

    def perform_destroy(self, instance):
        if instance.image:
            try:
                public_id = instance.image.split('/')[-1].split('.')[0]
                print(f"Đang xóa ảnh (do xóa sản phẩm) trên Cloudinary: {public_id}")
                cloudinary.uploader.destroy(public_id) 
            except Exception as delete_error:
               
                print(f"Lỗi xóa ảnh Cloudinary khi xóa sản phẩm {instance.id_product}: {delete_error}")
                
        print(f"Đã xóa sản phẩm: {instance.id_product}")
        super().perform_destroy(instance)
class WarehouseListAPI(ListAPIView):
    queryset = Warehouse.objects.all()  
    serializer_class = WarehouseSerializer
    permission_classes = [IsAdminUser]

# View để liệt kê danh sách sản phẩm
class WarehouseListAPIView(generics.ListAPIView): 
    queryset = Warehouse.objects.all().order_by('nameproduct')
    serializer_class = WarehouseSerializerList
    permission_classes = [IsAuthenticated]  
    authentication_classes = [SessionAuthentication]


class WarehouseCreateAPIView(generics.CreateAPIView):  
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = [IsAdminUser]  
    authentication_classes = [SessionAuthentication]

    def perform_create(self, serializer):
        image_file = self.request.FILES.get("image")
        image_url = None
        print(f"DEBUG: Đang xử lý tệp hình ảnh: {image_file}")

        
        if image_file:
            try:
                print(f"Đang tải ảnh lên Cloudinary: {image_file.name}")
                result = cloudinary.uploader.upload(
                    image_file,
                    folder="warehouse_images"
                )
                image_url = result.get("secure_url")  
                print(f"Tải ảnh thành công: {image_url}")
            except Exception as e:
                print(f"Lỗi tải ảnh lên Cloudinary: {e}")
                raise serializer.ValidationError({"image": f"Tải ảnh thất bại: {e}"})

        serializer.save(image=image_url)
        print(f"Đã tạo sản phẩm: {serializer.instance.id_product}")

def warehouse_list(request):
    warehouse_items = Warehouse.objects.all().order_by('nameproduct')  
    context = {
        'warehouse_items': warehouse_items
    }
    return render(request, 'app/warehouse_list.html', context)
