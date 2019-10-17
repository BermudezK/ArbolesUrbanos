from django.shortcuts import render

from .models import Tree
# Create your views here.


def edit_tree(request,value):
	Tree.quantity = value
	Tree.save()

	return


def show_tree(request):
	context = {}
	p = Tree.objects.all()
	context['arbol'] = p

	return render(request,'visualizacion.html',context)
