from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView
from django.shortcuts import redirect

from .models import Tree
# Create your views here.


def show_tree(request):
	context = {}
	p = Tree.objects.get(pk=1)
	context['arbol'] = p

	return render(request,'arbol/visualizacion.html',context)

# Vista del Usuario
def show_tree_user(request):
	context = {}
	p = Tree.objects.get(pk=1)
	context['arbol'] = p

	return render(request,'arbol/visualizacionUsuario.html',context)


def edit_tree(request):
	if request.POST:
		qty = int(request.POST.get("quantity"))
		arbol = Tree.objects.get(pk = request.POST.get("pk"))
		arbol.quantity += qty
		arbol.save()
	return redirect('arbol:show_tree')


class nuevo(CreateView):
	model = Tree
	template_name = 'arbol/nuevo.html'
	success_url = reverse_lazy('arbol:show_tree')
	fields = '__all__'
