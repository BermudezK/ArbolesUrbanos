from django import forms
from .models import Denuncia, PostInformativo, PostBase
from .utils import TipoDenunciaEnum



class CreateDenuncia(forms.ModelForm):
	tipo = forms.ChoiceField(choices=TipoDenunciaEnum.choices())
	text = forms.CharField(max_length=500)
	# falta definir el titulo para los posts
	class Meta:
		model = Denuncia
		fields = ['tipo', 'text', 'img']

class CreatePostInformativo(forms.ModelForm):
	text = forms.CharField(max_length=1000)
	class Meta:
		model = PostInformativo
		fields = ['text', 'img']

	def __init__(self, *args, **kwargs):
	 super(CreateDenuncia, self).__init__(*args, **kwargs)

	 self.fields['tipo'].widget = forms.ChoiceField(
		 attrs={'label':'Tipo de denuncia'})
	 self.fields['text'].widget = forms.CharField(
		 attrs={'label':'Descripción'})
	 self.fields['img'].widget = forms.ImageField(
		 attrs={'label':'Ingrese una imagen'})



