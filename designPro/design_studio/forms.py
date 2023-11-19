from .models import Request
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название заявки'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание заявки'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата заявки(YYYY-MM-DD)'
            })
        }