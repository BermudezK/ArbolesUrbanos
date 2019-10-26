from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage

from .forms import ContactForm

# Create your views here.
def Inicio (request):
    return render (request, 'core/home.html')

def denuncia (request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            surname = request.POST.get('surname', '')
            email = request.POST.get('email', '')
            subject = request.POST.get('subject', '')
            content = request.POST.get('content', '')

            #Enviamos el correo y redireccionamos
            email = EmailMessage(
                "Arboles Urbanos: Nueva Denuncia", #asunto
                "De: {} <{}>\n\n Asunto: {}\n\n Escribio:\n {}".format(name,email,subject,content), #cuerpo 
                "{}".format(email), #email_origen
                ["softwaremovement19@gmail.com"], #email_destino
                reply_to=[email]
            )
            
            #Suponemos que todo ha ido bien, entonces redireccionamos
            #return redirect(reverse('contact:contact')+"?ok")
            try:
                "Redireccionamos a OK"
                email.send()
                return redirect(reverse('denuncia')+"?ok")
            except:
                "Redireccionamos a FAIL"
                return redirect(reverse('denuncia')+"?fail")

    return render(request, 'core/denuncia.html',{'form':contact_form})

def contacto (request):
    print(request.user)

    contact_form = ContactForm()
    if not request.user == 'AnonymousUser':
        data={
            'name': request.POST.get('name'),
            'surname': request.POST.get('surname'),
            'email': request.POST.get('email'),
            'subject': request.POST.get('subject'),
            'content': request.POST.get('content'),
        }
    else:
        data={
            'name': request.user.first_name,
            'surname': request.user.last_name,
            'email': request.user.email,
            'subject': request.POST.get('subject', ''),
            'content': request.POST.get('content', ''),
        }

    if request.method == "POST":
        contact_form = ContactForm(data)
        if contact_form.is_valid():
            name = data.get('name')
            surname = data.get('surname')
            email = data.get('email')
            subject = data.get('subject')
            content = data.get('content')

            #Enviamos el correo y redireccionamos
            email = EmailMessage(
                "Arboles Urbanos: Nuevo mensaje de contacto", #asunto
                "De: {} <{}>\n\n Asunto: {}\n\n Escribio:\n {}".format(name,email,subject,content), #cuerpo 
                "{}".format(email), #email_origen
                ["softwaremovement19@gmail.com"], #email_destino
                reply_to=[email]
            )
            
            #Suponemos que todo ha ido bien, entonces redireccionamos
            #return redirect(reverse('contact:contact')+"?ok")
            try:
                "Redireccionamos a OK"
                email.send()
                return redirect(reverse('contacto')+"?ok")
            except:
                "Redireccionamos a FAIL"
                return redirect(reverse('contacto')+"?fail")

    return render(request, 'core/contacto.html',{'form':contact_form})




