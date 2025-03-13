from rest_framework import serializers
from .models import Check_out

class CheckOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Check_out
        fields = ['name_product', 'price', 'user_name']