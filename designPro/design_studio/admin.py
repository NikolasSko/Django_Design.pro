from django.contrib import admin
from .models import Request, Category

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
