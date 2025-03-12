from django import forms
from .models import Register  
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from .models import Don_hang
class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(),
        label="Nhập lại mật khẩu"
    )

    class Meta:
        model = Register
        fields = ['user_name', 'pass_word']  
        # help_texts = {
        #     'user_name': 'Tên đăng nhập không quá 100 ký tự',
        #     'pass_word': '1 chữ hoa, 1 ký tự đặc biệt ',
        # }
        widgets = {
            'pass_word': forms.PasswordInput(),
        }
        labels = {
            'user_name': 'Tên đăng nhập',
            'pass_word': 'Mật khẩu',
        }
    def clean(self):
        cleaned_data = super().clean()
        pass_word = cleaned_data.get("pass_word")
        confirm_password = cleaned_data.get("confirm_password")

        if pass_word and confirm_password and pass_word != confirm_password:
            raise forms.ValidationError("Mật khẩu không khớp!")

        return cleaned_data  

class LoginForm(forms.Form):
    user_name = forms.CharField(label="Tên đăng nhập", max_length=100)
    pass_word = forms.CharField(label="Mật khẩu", widget=forms.PasswordInput())
    
    def clean(self):
        cleaned_data = super().clean()
        user_name = cleaned_data.get("user_name")
        pass_word = cleaned_data.get("pass_word")   
        user = Register.objects.filter(user_name= user_name, pass_word= pass_word).first()
        if not user:
            raise forms.ValidationError("Tên đăng nhập hoặc mật khẩu không đúng!")
        return cleaned_data

class Don_hang(forms.ModelForm):
    class Meta:
        model = Don_hang
        fields = ['user_name', 'ten_don_hang', 'tong_tien',]
        labels = {
            'user_name': 'Người dùng',
            'ten_don_hang': 'Tên đơn hàng',
            'tong_tien': 'Tổng tiền',
        }
