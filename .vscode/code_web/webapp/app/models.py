from django.db import models
from django.contrib.auth.models import User
class Register(models.Model):
    user_name = models.CharField(primary_key = True,max_length=100)
    pass_word = models.CharField(max_length=100)
    
    class Meta:
        managed= False
        db_table = 'register'
class Don_hang(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    ten_don_hang = models.CharField(max_length=255)
    tong_tien = models.IntegerField()
    
    
