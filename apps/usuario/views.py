from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import User
from django.urls import reverse_lazy

class CreateUser(CreateView):
	model = User
	template_name = 'registerUser.html'
	succes_url = reverse_lazy('usuario:home')
	fields = '__all__'

class UpdateUser(UpdateView):
	model = User
	template_name = ''
	fields = ['password', 'birthday', 'cellphone', 'first_name', 'last_name']

class LoginUser():
	pass