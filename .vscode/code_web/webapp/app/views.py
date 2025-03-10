from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib import messages
from .forms import LoginForm
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

def logout_view(request):
    if "user_name" in request.session:
        del request.session["user_name"]  # Xóa user_name khỏi session
        messages.success(request, "Bạn đã đăng xuất thành công!")
    return redirect("home_page")  # Quay về trang chủ sau khi đăng xuất
