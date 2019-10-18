from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    email = models.EmailField(
    	'direccion de correo',
    	unique = True,
    	error_messages = {
    	'unique': 'Ya existe un usuario con ese email'
    	}
    )

    cellphone = models.CharField(max_length = 17, blank = True)
    birthday = models.DateField(auto_now=False, auto_now_add=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'birthday', 'username']
