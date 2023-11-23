from .models import Request, Category
from django.forms import ModelForm, TextInput, Textarea
from django import forms


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

class ChangeStatusForm(ModelForm):
    note = forms.CharField(required=False)
    design = forms.ImageField(required=False)

    class Meta:
        model = Request
        fields = ['status', 'note', 'design']

    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get('status')
        note = cleaned_data.get('note')
        design = cleaned_data.get('design')

        if status == 'employed' and not note:
            self.add_error('comment', 'Комментарий обязателен при смене статуса на "Принято в работу".')
        elif status == 'Done' and not design:
            self.add_error('design', 'Дизайн обязателен при смене статуса на "Выполнено".')
