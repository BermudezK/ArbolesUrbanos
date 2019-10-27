from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu Nombre','id':'username'}
    ), min_length=3, max_length=30)

    surname = forms.CharField(label="Apellido", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu Apellido','id':'surname'}
    ), min_length=3, max_length=30)

    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control', 'placeholder':'Escribe tu Email','id':'email'}
    ), min_length=3, max_length=100)

    subject = forms.CharField(label="Asunto", required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe un Asunto','id':'subject'}
    ), min_length=3, max_length=30)
    
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(
      attrs={'class':'form-control', 'rows':4, 'placeholder':'Escribe tu Mensaje','id':'content'}  
    ), min_length=5, max_length=250)