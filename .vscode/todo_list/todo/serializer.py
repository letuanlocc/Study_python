from rest_framework import serializers
from .models import Todo
from django.contrib.auth.models import User
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"]
        )
class TodoSerializer(serializers.ModelSerializer):
    priority_display = serializers.CharField(source='get_priority_display', read_only=True)
    class Meta:
        model = Todo
        fields = ['id', 'title', 'completed', 'created_at', 'priority_display']
        
        extra_kwargs = {
            'priority_display': {'required': False},
            'created_at': {'read_only': True},
        }
    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty.")
        if len(value) > 100:
            raise serializers.ValidationError("Title cannot exceed 100 characters.")
        return value
    