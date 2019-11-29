from django import forms
from .models import Denuncia, PostInformativo, PostBase, PostImg
from .utils import TipoDenunciaEnum



class CreateDenunciaForm(forms.ModelForm):
	tipo = forms.ChoiceField(choices=TipoDenunciaEnum.choices())
	# falta definir el titulo para los posts
	class Meta:
		model = Denuncia
		fields = ['titulo','tipo', 'text','email']

class ImagenForm(forms.ModelForm):

	class Meta:
		model = PostImg
		fields = ['img']

class CreatePostInformativo(forms.ModelForm):
	
	class Meta:
		model = PostInformativo
		fields = ['text']




