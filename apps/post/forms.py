from django import forms
from .models import Denuncia, PostInformativo, PostBase
from .utils import TipoDenunciaEnum


class BaseForm(forms.ModelForm):
	class Meta:
		model = PostBase
		fields = ['img']

class CreateDenuncia(BaseForm):
	tipo = forms.ChoiceField(choices=TipoDenunciaEnum.choices())
	text = forms.CharField(max_length=500)

	class Meta:
		model = Denuncia
		fields = ['tipo', 'text']

class CreatePostInformativo(BaseForm):
	text = forms.CharField(max_length=1000)

	class Meta:
		model = PostInformativo
		fields = ['text']


