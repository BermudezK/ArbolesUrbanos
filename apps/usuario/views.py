from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django import forms
from .forms import UserCreateFormWithEmail

User = get_user_model()

class UpdateUser(UpdateView):
	model = User
	template_name = ''
	fields = ['email', 'username', 'password']

class SignUpView(CreateView):
    form_class = UserCreateFormWithEmail
    template_name = 'User/registerUser.html'
    success_url = reverse_lazy('home')
    
