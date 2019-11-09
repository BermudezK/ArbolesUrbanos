from django.contrib import admin
from django.urls import path
from . import views

app_name = 'arbol'

urlpatterns = [
	path('arboles/',views.show_tree, name = 'show_tree'), 
	path('nuevo/',views.nuevo.as_view(), name = 'nuevo'),
	path('editar/',views.edit_tree, name = 'edit_tree'), #Este no lo necesitariamos ya que solo muestra un label con la info

	# Usuario
	path('show/',views.show_tree_user, name = "show_tree_user"),
	
]