from django import forms
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from .models import Warehouse
class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(),
        label="Nhập lại mật khẩu"
    )

    class Meta:
        model = User  
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
        labels = {
            'username': 'Tên đăng nhập',
            'password': 'Mật khẩu',
        }
        help_texts = {  # Thêm hướng dẫn cho username
            'username': 'Chỉ chứa chữ cái, số và các ký tự @ . + - _ (Tối đa 150 ký tự)',
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Mật khẩu không khớp!")

        return cleaned_data  

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data["password"])  # Hash password
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    user_name = forms.CharField(label="Tên đăng nhập", max_length=100)
    pass_word = forms.CharField(label="Mật khẩu", widget=forms.PasswordInput())
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("user_name")
        password = cleaned_data.get("pass_word")   
        user = User.objects.filter(username= username).first()
        if not user or not check_password(password, user.password):
            raise forms.ValidationError("Tên đăng nhập hoặc mật khẩu không đúng!")
        return cleaned_data

# class Warehouse(forms.ModelForm):
#     class Meta:
#         model = Warehouse
#         fields = ['nameproduct', 'price']
