from django import forms
from .models import Denuncia, PostInformativo, PostBase, PostImg
from .utils import TipoDenunciaEnum



class CreateDenunciaForm(forms.ModelForm):
	tipo = forms.ChoiceField(choices=TipoDenunciaEnum.choices())
	text = forms.CharField(max_length=500, widget=forms.Textarea(attrs={"class":"form-control"}))
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

	def __init__(self, *args, **kwargs):
	 super(CreateDenuncia, self).__init__(*args, **kwargs)
	 self.fields['tipo'].widget = forms.ChoiceField(
		 attrs={'class':'form-control'})
	 self.fields['text'].widget = forms.CharField(
		 attrs={'class':'form-control'})
	 self.fields['img'].widget = forms.ImageField(
		 attrs={'class':'form-control'})



