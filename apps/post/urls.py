from django.urls import path
from . import views

urlpatterns = [
	
	# Urls to create posts
	path('create-denuncia/', views.CreateDenuncia.as_view(), name='create-denuncia'),
	path('create-info/', views.CreatePostInformativo.as_view(), name='create-info'),

	# Urls to lists posts
	path('denuncia/', views.listar, name='denuncia-home'),
	path('info/', views.ListPostInformativo.as_view(), name='info-home'),

]
