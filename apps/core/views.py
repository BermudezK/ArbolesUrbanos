from django.shortcuts import render, redirect
from django.urls import reverse_lazy
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


def contacto(request):
    data = None
    if request.user.is_authenticated:
        data = {
            'name': request.user.first_name,#POST.get('name'),
            'surname': request.user.last_name,#POST.get('surname'),
            'email': request.user.email,#POST.get('email'),
        }

    contact_form = ContactForm(data)
    if request.method == "POST":
        data = {
            'name': request.POST.get('name'),
            'surname': request.POST.get('surname'),
            'email': request.POST.get('email'),
            'subject': request.POST.get('subject'),
            'content': request.POST.get('content'),
        }
        contact_form = ContactForm(data=data, is_post=True)
        if contact_form.is_valid():
            # Enviamos el correo y redireccionamos
            email = EmailMessage(
                "Arboles Urbanos: Nuevo mensaje de contacto",  # asunto
                "De: {} <{}>\n\n Asunto: {}\n\n Escribio:\n {}".format(
                    data['name'], data['email'], data['subject'], data['content']),  # cuerpo
                "{}".format(data['email']),  # email_origen
                ["softwaremovement19@gmail.com"],  # email_destino
                reply_to=[data['email']]
            )

            # Suponemos que todo ha ido bien, entonces redireccionamos
            # return redirect(reverse('contact:contact')+"?ok")
            try:
                "Redireccionamos a OK"
                email.send()
                return redirect(reverse_lazy('contacto')+"?ok")
            except:
                "Redireccionamos a FAIL"
                return redirect(reverse_lazy('contacto')+"?fail")

    return render(request, 'core/contacto.html', {'form': contact_form})
