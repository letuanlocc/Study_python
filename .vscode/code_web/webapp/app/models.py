from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

    
class Warehouse(models.Model):
    id_product = models.CharField(max_length=50, primary_key=True)
    nameproduct = models.CharField(max_length=50)
    price = models.IntegerField()
    origin = models.CharField(max_length=40)
    instock = models.IntegerField()
    date_time = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.id_product
    
    class Meta:
        db_table = 'warehouse'
        
class Checkout(models.Model):
    id_checkout = models.AutoField(primary_key=True)  
    id_product = models.ForeignKey(Warehouse, on_delete=models.CASCADE, db_column='id_product')
    id_username = models.ForeignKey(User, on_delete=models.CASCADE, db_column='id_username')
    username = models.CharField(max_length=150)
    nameproduct = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField(null=True, blank=    True)  
    date_time = models.DateField(auto_now_add=True) 
    class Meta:
        db_table = 'Checkout'
