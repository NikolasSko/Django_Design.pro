from django.shortcuts import render
from django.views.generic.base import View
from .models import Request


class Index(View):
    def get(self, request):
        requests = Request.objects.all().order_by('-date')[:4]
        return render(request, 'index.html', {'request_list': requests})

class Profile(View):
    def get(self, request):
        return render(request, 'accounts/profile.html')

