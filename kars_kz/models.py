from django.db import models
from django.contrib.auth.models import AbstractUser


class Post(models.Model):
    title = models.CharField(max_length=22, verbose_name='Название')
    description = models.TextField(max_length=44, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')  
    quantity = models.PositiveIntegerField(verbose_name='Количество')  
    image_path = models.ImageField(upload_to='posts/', blank=True, null=True, verbose_name='Фото')  

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30, blank=True, null=True, verbose_name='Имя')
    last_name = models.CharField(max_length=30, blank=True, null=True, verbose_name="Фамилия")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
