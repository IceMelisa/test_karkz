from django.db import models
from django.contrib.auth.models import AbstractUser



class Post(models.Model):
    title = models.CharField(max_length=22)
    description = models.TextField(max_length=44)


    def __str__(self):
        return self.title


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30, blank=True, null=True) 
    last_name = models.CharField(max_length=30, blank=True, null=True)   

    def __str__(self):
        return self.username








