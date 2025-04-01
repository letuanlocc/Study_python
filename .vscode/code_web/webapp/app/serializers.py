from rest_framework import serializers
from .models import Checkout
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
import sys
from django.contrib.auth import get_user_model
class CheckOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = ['id_product','id_username','nameproduct', 'price', 'quantity', 'date_time']
