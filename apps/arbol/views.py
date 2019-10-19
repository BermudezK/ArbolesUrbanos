from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView

from .models import Tree
# Create your views here.

"""
def edit_tree(request,value):
	Tree.quantity = value
	Tree.save()

	return
"""

def show_tree(request):
	context = {}
	p = Tree.objects.get(pk=1)
	context['arbol'] = p

	return render(request,'arbol/visualizacion.html',context)


class edit_tree(UpdateView):
	model = Tree
	template_name = 'arbol/visualizacion.html'
	


class nuevo(CreateView):
	model = Tree
	template_name = 'arbol/nuevo.html'
	success_url = reverse_lazy('arbol:show_tree')
	fields = '__all__'