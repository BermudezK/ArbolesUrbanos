from django.urls import path
from . import views

urlpatterns = [
	
	# Urls to create posts
	# path('create-denuncia/', views.CreateDenuncia.as_view(), name='create-denuncia'),
	# path('create-info/', views.CreatePostInformativo.as_view(), name='create-info'),
	path('create-info/', views.CreatePostInfor, name='create-info'),
	path('create-denuncia/', views.CreateDenunciaa, name='create-denuncia'),

	# Urls to lists posts
	path('', views.listar, name='denuncia-home'),
	path('informacion/', views.ListPostInformativo.as_view(), name='info'),
	path('denuncias/', views.ListPostDenuncia.as_view(), name='denuncia'),
	path('eventos/', views.ListPostEventos.as_view(), name='evento-home'),

]
