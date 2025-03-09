from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib import messages
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