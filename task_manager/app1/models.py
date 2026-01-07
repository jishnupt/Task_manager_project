from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(unique=True)

    ROLE_CHOICE = (
        ('admin','admin'),
        ('user','user'),
    )
    role = models.CharField(max_length=50,choices=ROLE_CHOICE,default='user')

class Task(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    STATUS_CHOICE = (
        ('pending','pending'),
        ('done','done')
    )
    status = models.CharField(max_length=40,choices=STATUS_CHOICE,default='pending')
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='tasks')

    def __str__(self):
        return self.name
