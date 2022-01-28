from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

# Create your models here.


class CustomUser(AbstractUser):

    email = models.EmailField(('Email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']

    objects = CustomUserManager()

    def __str__(self):
        return f"Name : {self.first_name}, Email: {self.email}"


class UserFile(models.Model):
    title = models.CharField(max_length=32)
    file = models.FileField(upload_to='')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"upload-ID-{self.id}-{self.title}-{self.timestamp}"
