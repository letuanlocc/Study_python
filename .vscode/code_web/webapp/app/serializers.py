from rest_framework import serializers
from .models import Check_out
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
        user = self.context['request'].user  # Lấy user từ request
        validated_data['user_name'] = user  # Gán user vào dữ liệu
        return super().create(validated_data)
    