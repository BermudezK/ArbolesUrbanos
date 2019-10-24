#Formulario extendido de UserCreationForm

from django import forms
from apps.usuario.models import User
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):

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

    class Meta:
        model=User
        fields = '__all__'
        
    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)

        user.username = self.cleaned_data["username"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        user.cellphone = self.cleaned_data["cellphone"]
        user.birthday = self.cleaned_data["birthday"]
        user.password1 = self.cleaned_data["password1"]
        user.password2 = self.cleaned_data["password2"]
        if commit:
            user.save()
        return user

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya se encuentra registrando, intente nuevamente.")
        return email

