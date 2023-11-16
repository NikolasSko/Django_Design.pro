from django.shortcuts import render
from django.views.generic.base import View
from .forms import RegisterUserForm

class Login(View):
    def get(self, request):
        return render(request, 'accounts/login.html')

def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)  # создание объекта без сохранения в БД
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'accounts/registration_done.html')
    else:
        form = RegisterUserForm()
    return render(request, 'accounts/registration.html', {'form': form})

