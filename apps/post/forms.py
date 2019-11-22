from django import forms
from .models import Denuncia, PostInformativo, PostBase, PostImg
from .utils import TipoDenunciaEnum



class CreateDenunciaForm(forms.ModelForm):
	tipo = forms.ChoiceField(choices=TipoDenunciaEnum.choices())
	text = forms.CharField(max_length=500)
	# falta definir el titulo para los posts
	class Meta:
		model = Denuncia
		fields = ['titulo','tipo', 'text']

class ImagenForm(forms.ModelForm):

	class Meta:
		model = PostImg
		fields = ['img']

class CreatePostInformativo(forms.ModelForm):
	text = forms.CharField(max_length=1000)
	class Meta:
		model = PostInformativo
		fields = ['text']


