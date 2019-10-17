#Formulario extendido de UserCreationForm

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from django.contrib.auth.models import User

class UserCreateFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Campo obligatorio. Maximo de 250 caracteres")
    cellphone = forms.CharField(max_length = 17)
    birthday = forms.DateField()

    class Meta:
        model = User
        fields = ('username', 'email', 'cellphone', 'birthday', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya se encuentra registrando, intente nuevamente.")
        return email