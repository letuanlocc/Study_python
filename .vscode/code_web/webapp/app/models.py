from django.db import models
from django.contrib.auth.models import User
class Check_out(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE,db_column='user_name')
    name_product = models.CharField(max_length=50)
    price = models.IntegerField()
    
    # @property
    # def total(self):
    #     return Check_out.objects.aggregate(total=models.Sum(models.F('price')))['total'] #ra 45000 thay vi {total: 45000}
    
    class Meta:
        db_table = 'Check_out'
    
