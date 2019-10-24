from django.contrib import admin
from django.urls import path
from . import views

app_name = "usuario"

urlpatterns = [
    path('', views.SignUpView.as_view(), name = 'register'),
    # path('', views.LoginUser.as_view(), name = 'login')
    
]