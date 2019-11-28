from django.urls import path
from . import views

urlpatterns = [
	
	# Urls to create posts
	# path('create-denuncia/', views.CreateDenuncia.as_view(), name='create-denuncia'),

	path('crear-info/', views.CreatePostInformativo.as_view(), name='create-info'),
	path('crear-denuncia/', views.CreateDenunciaa, name='create-denuncia'),


	# Urls to lists posts
	path('', views.listar, name='denuncia-home'),
	path('informacion/', views.ListPostInformativo.as_view(), name='info'),
	# path('denuncias/', views.ListPostDenuncia.as_view(), name='denuncia'),
	path('denuncias/', views.ListarPostDenuncia, name='denuncia'),
	path('eventos/', views.ListPostEventos.as_view(), name='evento-home'),

]
