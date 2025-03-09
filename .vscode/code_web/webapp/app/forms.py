from django import forms
from .models import register

class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Nhập lại mật khẩu")
    
    class Meta:
        model = register
        fields = ['user_name', 'pass_word']
        widgets = {
            'pass_word': forms.PasswordInput()
        }
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("pass_word")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Mật khẩu không khớp!")