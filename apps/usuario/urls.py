from django.contrib import admin
from django.urls import path
from . import views

app_name = "usuario"

urlpatterns = [
    path('', views.CreateUser.as_view(), name="create"),
]