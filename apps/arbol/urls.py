from django.contrib import admin
from django.urls import path
from . import views

app_name = 'arbol'

urlpatterns = [
	
	path('Arboles/',views.show_tree, name = 'show_tree'),
	path('nuevo/',views.nuevo.as_view(), name = 'nuevo'),
	
]