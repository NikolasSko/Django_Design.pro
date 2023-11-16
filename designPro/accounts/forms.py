from django import forms
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator, EmailValidator


class RegisterUserForm(forms.ModelForm):
    fio = forms.CharField(label='ФИО', max_length=100, required=True, validators=[
        RegexValidator(
            regex=r'^[а-яА-ЯёЁ\s-]+$',
            message='Пожалуйста, используйте только кириллические буквы, пробелы и дефисы.'
        )
    ])
    username = forms.CharField(label='Логин', max_length=100, required=True, validators=[
        RegexValidator(
            regex=r'^[a-zA-Z-]+$',
            message='Пожалуйста, используйте только латиницу и дефис!'
        )
    ])
    email = forms.EmailField(required=True, validators=[
        EmailValidator(
            message='Введите корректную почту!'
        )
    ])
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput, required=True)
    approval = forms.BooleanField(label="Согласие на обработку данных", required=True)


    class Meta:
        model = get_user_model()
        fields = ['fio', 'username', 'email', 'password', 'password2', 'approval']
        labels = {
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }

        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError("Пароли не совпадают!")
            return cd['password2']