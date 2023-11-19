from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('create/', views.CreateRequestView.as_view(), name='create_request'),
]