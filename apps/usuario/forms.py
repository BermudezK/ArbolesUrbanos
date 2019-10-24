#Formulario extendido de UserCreationForm

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserCreateFormWithEmail(UserCreationForm):
	email = forms.EmailField(required=True, help_text="Campo obligatorio. Maximo de 250 caracteres")
	cellphone = forms.CharField(max_length = 17)
	birthday = forms.DateField()

	class Meta(UserCreationForm.Meta):
		model = User
		fields = ('email', 'first_name', 'last_name', 'username', 'birthday', 'cellphone')

	def __init__(self, *args, **kwargs):
		super(UserCreateFormWithEmail, self).__init__(*args, **kwargs)
		#Modificar en tiempo real
		self.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Nombre de Usuario'})

		self.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Dirección de Email'})

		self.fields['cellphone'].widget = forms.TextInput(attrs={'class':'form-control mb-2',' placeholder':'Celular'})

		self.fields['birthday'].widget = forms.DateInput(attrs={'class':'form-control mb-2',' placeholder':'Fecha de Nacimiento'})

		self.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2',' placeholder':'Contraseña'})

		self.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2',' placeholder':'Repite la contraseña'})


