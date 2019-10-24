from django.shortcuts import render

from django.urls import reverse_lazy
from .forms import SignUpForm
#from .forms import UserCreateFormWithEmail

User = get_user_model()

class UpdateUser(UpdateView):
	model = User
	template_name = ''
	fields = ['email', 'username', 'password']

class SignUpView(FormView):
    template_name = 'User/registerUser.html'

