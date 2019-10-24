from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import User
from django.urls import reverse_lazy
from django import forms
from .forms import UserCreateFormWithEmail
from django.core.mail import EmailMessage


class UpdateUser(UpdateView):
	model = User
	template_name = ''
	fields = ['password', 'birthday', 'cellphone', 'first_name', 'last_name']

class SignUpView(CreateView):
    form_class = UserCreateFormWithEmail
    template_name = 'User/registerUser.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        #Modificar en tiempo real
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Nombre de Usuario'})

        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Dirección de Email'})

        form.fields['cellphone'].widget = forms.TextInput(attrs={'class':'form-control mb-2',' placeholder':'Celular'})

        form.fields['birthday'].widget = forms.DateInput(attrs={'class':'form-control mb-2',' placeholder':'Fecha de Nacimiento'})

        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2',' placeholder':'Contraseña'})

        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2',' placeholder':'Repite la contraseña'})

        return form