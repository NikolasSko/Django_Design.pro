from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Request
from .forms import RequestForm


class Index(View):
    def get(self, request):
        requests = Request.objects.all().order_by('-date')[:4]
        progress_status = Request.objects.filter(status='employed').count()
        return render(request, 'index.html', {'request_list': requests, 'progress_status': progress_status})


def Profile(request):
    user = request.user  # Получаем авторизованного пользователя
    posts = Request.objects.filter(author=user)  # Фильтруем записи, где автор равен пользователю

    context = {
        'posts': posts
    }
    return render(request, 'accounts/profile.html', context)


class CreateRequestView(LoginRequiredMixin, CreateView):
    model = Request
    fields = ('name', 'description', 'category', 'image')
    template_name = 'accounts/create_request.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('profile')


def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class DetailRequest(DetailView):
    model = Request
    template_name = 'request/detail_request.html'
    context_object_name = 'request'

class UpdateRequest(UpdateView):
    model = Request
    template_name = 'accounts/create_request.html'
    fields = ('name', 'description', 'category', 'image')

class DeleteRequest(DeleteView):
    model = Request
    success_url = '/profile'
    template_name = 'request/delete_request.html'









