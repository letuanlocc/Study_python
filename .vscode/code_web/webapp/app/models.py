from django.db import models
class Register(models.Model):
    user_name = models.CharField(primary_key = True,max_length=100)
    pass_word = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'register'