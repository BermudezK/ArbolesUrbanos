from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage

from .forms import ContactForm

# Create your views here.
def Inicio (request):
    return render (request, 'core/home.html')

def contacto (request):
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
                "Arboles Urbanos: Nuevo mensaje de contacto", #asunto
                "De {} <{}>\n\nEscribio:\n\n{}".format(name,email,content), #cuerpo 
                "no-contestar@inbox.mailtrap.io", #email_origen
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

    return render(request, 'core/contact.html',{'form':contact_form})

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
                "Arboles Urbanos: Nuevo mensaje de contacto", #asunto
                "De {} <{}>\n\nEscribio:\n\n{}".format(name,email,content), #cuerpo 
                "no-contestar@inbox.mailtrap.io", #email_origen
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


