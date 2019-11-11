from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from apps.arbol.models import Tree

from .forms import ContactForm

# Create your views here.


def Inicio(request):
    # AGREGUE LAS 3 LINEAS SIGUIENTES DE CODIGO PARA PODER OBTENER EN TODO MOMENTO LA CANTIDAD DE ARBOLES PNATADOS POR LA ONG
    context = {}
    p = Tree.objects.get(pk=1)
    context['arbol'] = p
    return render(request, 'core/home.html', context)


def landing(request):
    # AGREGUE LAS 3 LINEAS SIGUIENTES DE CODIGO PARA PODER OBTENER EN TODO MOMENTO LA CANTIDAD DE ARBOLES PNATADOS POR LA ONG
    context = {}
    p = Tree.objects.get(pk=1)
    context['arbol'] = p
    return render(request, 'core/landing.html', context)


def contacto(request):
    print(request.user.get_all_permissions())
    contact_form = ContactForm()
    if not request.user == 'AnonymousUser':
        data = {
            'name': request.POST.get('name'),
            'surname': request.POST.get('surname'),
            'email': request.POST.get('email'),
            'subject': request.POST.get('subject'),
            'content': request.POST.get('content'),
        }
    else:
        data = {
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

            # Enviamos el correo y redireccionamos
            email = EmailMessage(
                "Arboles Urbanos: Nuevo mensaje de contacto",  # asunto
                "De: {} <{}>\n\n Asunto: {}\n\n Escribio:\n {}".format(
                    name, email, subject, content),  # cuerpo
                "{}".format(email),  # email_origen
                ["softwaremovement19@gmail.com"],  # email_destino
                reply_to=[email]
            )

            # Suponemos que todo ha ido bien, entonces redireccionamos
            # return redirect(reverse('contact:contact')+"?ok")
            try:
                "Redireccionamos a OK"
                email.send()
                return redirect(reverse('contacto')+"?ok")
            except:
                "Redireccionamos a FAIL"
                return redirect(reverse('contacto')+"?fail")

    return render(request, 'core/contacto.html', {'form': contact_form})
