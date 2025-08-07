from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('add/', views.add_task, name='add_task'),
    path('update/<int:pk>/', views.update_task, name='update_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('complete/<int:pk>/', views.complete_task, name='complete_task'),
]