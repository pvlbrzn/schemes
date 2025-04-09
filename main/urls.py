from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='home'),
    path('create/', views.create_schema, name='create_schema'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('after-login/', views.after_login_redirect, name='after_login'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
]
