from django.db import models
from django.contrib.auth import get_user_model

class Request(models.Model):
    CATEGORY_CATEGORY = [
        ('house', 'жилой_дом'),
        ('building', 'здание'),
        ('not-stated', 'не известно')
    ]
    category = models.CharField(max_length=254, verbose_name='Статус', choices=CATEGORY_CATEGORY, default='not-stated')
    name = models.CharField('Название заявки', max_length=100)
    description = models.TextField('Описание заявки')
    image = models.ImageField('Изображение помещения', upload_to='image/%Y')
    CATEGORY_STATUS = [
        ('New', 'новая'),
        ('Done', 'выполненная'),
        ('employed', 'принятая в работу')
    ]
    status = models.CharField(max_length=254, verbose_name='Статус', choices=CATEGORY_STATUS, default='New')
    date = models.DateField('Дата публикации заявки')

    def __str__(self):
        return f'{self.name} {self.date}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
