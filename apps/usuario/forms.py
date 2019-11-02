#Formulario extendido de UserCreationForm

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserCreateFormWithEmail(UserCreationForm):
	first_name = forms.CharField(max_length = 30,  min_length = 3)
	last_name = forms.CharField(max_length = 30, min_length = 3)
	email = forms.EmailField(required=True, help_text="Campo obligatorio. Maximo de 250 caracteres")
	cellphone = forms.CharField(max_length = 10)
	birthday = forms.DateField()

	class Meta(UserCreationForm.Meta):
		model = User
		fields = ('email', 'first_name', 'last_name', 'username', 'birthday', 'cellphone')
		help_texts={
			'username': None,
		}

	def __init__(self, *args, **kwargs):
		super(UserCreateFormWithEmail, self).__init__(*args, **kwargs)
		#Modificar en tiempo real
		self.fields['first_name'].widget = forms.TextInput(
			attrs={'class':'form-control mb-2','placeholder':'Nombre',
			'aria-describedby':'first_nameHelpText',
			'minlength':'3', 'maxlength':'30',
			'pattern':'[a-zA-Z]'})
		self.fields['last_name'].widget = forms.TextInput(
			attrs={'class':'form-control mb-2','placeholder':'Apellido',
			'aria-describedby':'lastnameHelpText',
			'minlength':'3', 'maxlength':'30',
			'pattern':'[a-zA-Z]'})
		self.fields['username'].widget = forms.TextInput(
			attrs={'class':'form-control mb-2','placeholder':'Nombre de Usuario',
			'aria-describedby':'usernameHelpText',
			'minlength':'6', 'maxlength':'8',
			'pattern':'^[a-zA-Z][a-zA-Z0-9-_\.]{6,8}$'})

		self.fields['email'].widget = forms.EmailInput(
			attrs={'class':'form-control mb-2', 'placeholder':'ejemplo@email.com'})

		self.fields['cellphone'].widget = forms.TextInput(
			attrs={'class':'form-control mb-2',' placeholder':'3624112233',
			'aria-describedby':'cellphoneHelpText'})

		self.fields['birthday'].widget = forms.DateInput(
			attrs={'class':'form-control mb-2',' placeholder':'dd/mm/aaaa',
			'pattern':'(0[1-9]|1[0-9]|2[0-9]|3[01]).(0[1-9]|1[012]).[0-9]{4}'})

		self.fields['password1'].widget = forms.PasswordInput(
			attrs={'class':'form-control mb-2',' placeholder':'Contraseña',
			'aria-describedby':'password1HelpText'})

		self.fields['password2'].widget = forms.PasswordInput(
			attrs={'class':'form-control mb-2',' placeholder':'Contraseña'})


