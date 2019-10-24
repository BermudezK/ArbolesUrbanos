#Formulario extendido de UserCreationForm

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserCreateFormWithEmail(UserCreationForm):
	# email = forms.EmailField(required=True, help_text="Campo obligatorio. Maximo de 250 caracteres")
	# cellphone = forms.CharField(max_length = 17)
	# birthday = forms.DateField()

    username =forms.CharField(label="Nombre de Usuario:", required=True, widget=forms.TextInput(
    attrs={'placeholder':'Escribe tu usuario'}
    ), min_length=3, max_length=100) 
    
    first_name=forms.CharField(label="Nombre:", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu nombre'}
    ), min_length=3, max_length=30)

    last_name=forms.CharField(label="Apellido:", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu apellido'}
    ), min_length=3, max_length=30)

    email = forms.EmailField(label="Email:", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'ejemplo@gmail.com'}
    ), min_length=3, max_length=100)

    cellphone = forms.CharField(label="Celular:", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'3624112233'}
    ), min_length=3, max_length=30)
    
    birthday = forms.DateField(label="Fecha de Nacimiento:", required=True, widget=forms.DateInput(
      attrs={'class':'form-control', 'rows':2, 'placeholder':'dd/mm/aaaa'}  
    ))

    password1 = forms.CharField(label="Contraseña:", required=True, widget=forms.PasswordInput(
      attrs={'class':'form-control', 'rows':2, 'placeholder':'Escribe tu contraseña'}  
    ), min_length=5, max_length=25)

    password2 = forms.CharField(label="Confirmar contraseña:", required=True, widget=forms.PasswordInput(
      attrs={'class':'form-control', 'rows':2, 'placeholder':'Repite tu contraseña'}  
    ), min_length=5, max_length=25)

