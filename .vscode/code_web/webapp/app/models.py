from django.db import models
class register(models.Model):
    user_name = models.CharField(primary_key = True,max_length=100)
    pass_word = models.CharField(max_length=100)
    
    class meta:
        manager = False
        db_table = 'register'