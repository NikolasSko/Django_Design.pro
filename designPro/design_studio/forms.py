from .models import Request
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

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