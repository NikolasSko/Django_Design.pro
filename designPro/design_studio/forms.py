from .models import Request, Category
from django.forms import ModelForm, TextInput, Textarea

class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ('name', 'description', 'category', 'image')

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название заявки'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание заявки'
            }),
        }


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name_category',)

        widgets = {
            'name_category': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название категории'
            })
        }
