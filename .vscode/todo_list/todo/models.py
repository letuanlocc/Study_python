from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Priority(models.IntegerChoices):
        HIGH = 1, 'High'
        MEDIUM = 2, 'Medium'
        LOW = 3, 'Low'
        
    priority = models.IntegerField(
        choices=Priority.choices,
        default=Priority.MEDIUM,
    )
    def __str__(self):
       return self.title

