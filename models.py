from django.db import models
from django.contrib.auth.models import User



class Todo(models.Model):
    status_choices=[
        ('C','COMPLETED'),
        ('P','PENDING'),
    ]
   
    title=models.CharField(max_length=30)
    status=models.CharField(max_length=30,choices=status_choices)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    priority=models.CharField(max_length=50)
    
# Create your models here.
