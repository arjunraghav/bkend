from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

# Create your models here.


def filename_naming_handler(instance, filename):
    extension = filename.split('.')[-1]
    return f"upload-ID-{instance.user_id}-{instance.title}-{instance.timestamp}.{extension}"


class CustomUser(AbstractUser):

    email = models.EmailField(('Email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']

    objects = CustomUserManager()

    def __str__(self):
        return f"Name : {self.first_name}, Email: {self.email}"


class UserFile(models.Model):

    id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    timestamp = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to=filename_naming_handler)

    def __str__(self):
        return f"upload-ID-{self.user_id}-{self.title}-{self.timestamp}"
