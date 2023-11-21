from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('profile/', views.Profile, name='profile'),
    path('create/', views.CreateRequestView.as_view(), name='create_request'),
    path('<int:pk>', views.DetailRequest.as_view(), name='detail_request'),
    path('<int:pk>/update', views.UpdateRequest.as_view(), name='update_request'),
    path('request/<int:pk>/delete', views.DeleteRequest.as_view(), name='delete_request'),
    path('admin/', views.adminPanel, name='admin'),
]