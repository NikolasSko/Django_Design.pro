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
    path('admin/', views.AdminPanel.as_view(), name='admin'),
    path('request/create_category/', views.CreateCategoryView.as_view(), name='create_category'),
    path('request/<int:category_id>/delete_category', views.delete_category, name='delete_category'),
    path('request/<int:pk>/change_status/', views.ChangeStatusView.as_view(),
         name='change_status'),
]