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
from .forms import Register
# from .models import Don_hang
# Create your views here.
def home(request):
    return render(request, 'app/home.html')
def milk_view(request):
    return render(request, 'app/milk.html')
def link_view(request):
    return render(request, 'app/link.html')
def menu_view(request):
    return render(request, 'app/menu.html') 
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Đăng ký thành công! Hãy đăng nhập.")
        else:
            messages.error(request, "Có lỗi xảy ra, vui lòng kiểm tra lại.")
    else:
        form = RegisterForm()

    return render(request, "app/register.html", {"form": form})
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data["user_name"]
            request.session["user_name"] = user_name
            messages.success(request, f"Chào mừng {user_name}, bạn đã đăng nhập thành công!")
            return redirect("home_page")  # Chuyển hướng sau khi đăng nhập thành công
        else:
            messages.error(request, "Tên đăng nhập hoặc mật khẩu không đúng!")
    else:
        form = LoginForm()

    return render(request, "app/login.html", {"form": form})
# def get_user_id_from_session(request):
#     user_name = request.session.get('user_name')  # Lấy user_name từ session
#     if user_name:
#         try:
#             user = Register.objects.get(user_name=user_name)  # Tìm user trong DB
#             return user.id  # Lấy ID của user
#         except ObjectDoesNotExist:
#             return None  # Không tìm thấy user trong database
#     return None  # Không có user_name trong session

def logout_view(request):
    if "user_name" in request.session:
        del request.session["user_name"]  # Xóa user_name khỏi session
        messages.success(request, "Bạn đã đăng xuất thành công!")
    return redirect("home_page")  # Quay về trang chủ sau khi đăng xuất

class CheckOutAPIView(APIView):     
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
