from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import User
from django.urls import reverse_lazy

class CreateUser(CreateView):
	model = User
	template_name = 'resgister'
	succes_url = reverse_lazy('usuario:home')
	fields = ''

class UpdateUser(UpdateView):
	model = User
	template_name = ''
	fields = ['password', 'birthday', 'cellphone', 'first_name', 'last_name']