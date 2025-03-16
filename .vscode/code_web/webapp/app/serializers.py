from rest_framework import serializers
from .models import Check_out
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
class CheckOutSerializer(serializers.ModelSerializer):
    valid_product = ['Em meo', 'Em vit hanh', 'Empe']
    class Meta:
        model = Check_out
        fields = ['name_product', 'price']
    def validate_price(self,value):
        if value < 0:
            raise serializers.ValidationError("Giá không hợp lệ")
        return value
    def validate_name_product(self,value):
        if value not in self.valid_product:
            raise serializers.ValidationError("Tên sản phẩm không hợp lệ")
        return value
    def create(self, validated_data):
        request = self.context.get('request') # Lấy user từ request
        if request:
            user = request.session.get('user_name') 
            if user:
                try:
                    user = User.objects.get(user_name= user)  # Truy vấn user
                    validated_data['user_name'] = user  # Gán object user vào
                except ObjectDoesNotExist:  
                    raise ValueError(f"Không tìm thấy user '{user}' trong Register")
                # Lấy user từ session
            validated_data['user_name'] = user  # Gán user vào dữ liệu
        return super().create(validated_data)
    