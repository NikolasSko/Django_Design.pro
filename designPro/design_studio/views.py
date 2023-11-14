from django.shortcuts import render
from django.views.generic.base import View
from .models import Request
from .forms import RegisterUserForm

class Index(View):
    def get(self, request):
        requests = Request.objects.all().order_by('-date')[:4]
        return render(request, 'index.html', {'request_list': requests})

class Login(View):
    def get(self, request):
        return render(request, 'registration/login.html')

def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # создание объекта без сохранения в БД
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'registration/registration_done.html')
    else:
        form = RegisterUserForm()
    return render(request, 'registration/registration.html', {'form': form})