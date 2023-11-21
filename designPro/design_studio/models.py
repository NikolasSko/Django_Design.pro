from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Request(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default= "" )
    name = models.CharField('Название заявки', max_length=100)
    description = models.TextField('Описание заявки')
    image = models.ImageField('Изображение помещения', upload_to='image/%Y')
    CATEGORY_STATUS = [
        ('New', 'новая'),
        ('Done', 'выполненная'),
        ('employed', 'принятая в работу')
    ]
    status = models.CharField(max_length=254, verbose_name='Статус', choices=CATEGORY_STATUS, default='New')
    date = models.DateTimeField('Дата публикации', default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'{self.name} {self.date}'

    def get_absolute_url(self):
        return f'/request/{self.id}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
