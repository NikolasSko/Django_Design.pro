# Generated by Django 4.2.6 on 2023-11-19 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design_studio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterField(
            model_name='request',
            name='date',
            field=models.DateField(default='17-09-2004', verbose_name='Дата публикации'),
        ),
    ]
