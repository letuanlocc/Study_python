from django.db import models
from django.contrib.auth.models import User
class Checkout(models.Model):
    id_username = models.ForeignKey(User, on_delete=models.CASCADE, db_column='id_username') 
    id_checkout = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150)
    nameproduct = models.CharField(max_length=50)
    price = models.IntegerField()
    
    # @property
    # def total(self):
    #     return Check_out.objects.aggregate(total=models.Sum(models.F('price')))['total'] #ra 45000 thay vi {total: 45000}
    
    class Meta:
        db_table = 'Checkout'
    
