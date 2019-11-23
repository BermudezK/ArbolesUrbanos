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

    def __init__(self, user=None, is_post=False,*args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['name'].initial = user['name']
            self.fields['name'].widget.attrs['readonly'] = True

            self.fields['surname'].initial = user['surname']
            self.fields['surname'].widget.attrs['readonly'] = True

            self.fields['email'].initial = user['email']
            self.fields['email'].widget.attrs['readonly'] = True

            if is_post:
                self.fields['subject'].initial = user['subject']
                self.fields['subject'].widget.attrs['readonly'] = True

                self.fields['content'].initial = user['content']
                self.fields['content'].widget.attrs['readonly'] = True