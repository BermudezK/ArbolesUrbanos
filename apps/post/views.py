# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .forms import CreateDenunciaForm, CreatePostInformativo, ImagenForm
from .models import Denuncia, PostInformativo, PostImg
from apps.arbol.models import Tree
from apps.usuario.models import User




def CreateDenunciaa(request):

	if request.user.is_authenticated:
		usuario = User.objects.get(email = request.user)

		if request.method == 'GET':
			form = CreateDenunciaForm()
			form2 = ImagenForm()
		else:
			form = CreateDenunciaForm(request.POST)
			form2 = ImagenForm(request.POST, request.FILES)
			if form.is_valid() and form2.is_valid():
				d = form.save(commit = False)
				
				d.created_by = usuario
				d.titulo = request.POST.get('titulo')
				d.tipo = request.POST.get('tipo')
				d.text = request.POST.get('text')
				d.email = usuario.email
				d.save()

				denuncia = Denuncia.objects.get(pk = d.pk)
				if request.POST.get('img') != '':
					i = form2.save(commit = False)
					i.post = denuncia
					i.img = request.FILES.get('img')
					i.save()

				if request.POST.get('img2') != '':
					form2 = ImagenForm(request.POST, request.FILES)
					i = form2.save(commit = False)
					i.post = denuncia
					i.img = request.FILES.get('img2')
					i.save()

				if request.POST.get('img3') != '':
					form2 = ImagenForm(request.POST, request.FILES)
					i = form2.save(commit = False)
					i.post = denuncia
					i.img = request.FILES.get('img3')
					i.save()

				if request.POST.get('img4') != '':
					form2 = ImagenForm(request.POST, request.FILES)
					i = form2.save(commit = False)
					i.post = denuncia
					i.img = request.FILES.get('img4')
					i.save()

				if request.POST.get('img5') != '':
					form2 = ImagenForm(request.POST, request.FILES)
					i = form2.save(commit = False)
					i.post = denuncia
					i.img = request.FILES.get('img5')
					i.save()

			redirecion = redirect(reverse('denuncia'))
			return redirecion

	else:
		if request.method == 'GET':
			form = CreateDenunciaForm()
			form2 = ImagenForm()
		else:
			form = CreateDenunciaForm(request.POST)
			form2 = ImagenForm(request.POST, request.FILES)
			if form.is_valid() and form2.is_valid():
				d = form.save(commit = False)
				
				d.titulo = request.POST.get('titulo')
				d.tipo = request.POST.get('tipo')
				d.text = request.POST.get('text')
				d.email = request.POST.get('email')
				d.save()

				denuncia = Denuncia.objects.get(pk = d.pk)
				if request.POST.get('img') != '':
					i = form2.save(commit = False)
					i.post = denuncia
					i.img = request.FILES.get('img')
					i.save()

				if request.POST.get('img2') != '':
					form2 = ImagenForm(request.POST, request.FILES)
					i = form2.save(commit = False)
					i.post = denuncia
					i.img = request.FILES.get('img2')
					i.save()

				if request.POST.get('img3') != '':
					form2 = ImagenForm(request.POST, request.FILES)
					i = form2.save(commit = False)
					i.post = denuncia
					i.img = request.FILES.get('img3')
					i.save()

				if request.POST.get('img4') != '':
					form2 = ImagenForm(request.POST, request.FILES)
					i = form2.save(commit = False)
					i.post = denuncia
					i.img = request.FILES.get('img4')
					i.save()

				if request.POST.get('img5') != '':
					form2 = ImagenForm(request.POST, request.FILES)
					i = form2.save(commit = False)
					i.post = denuncia
					i.img = request.FILES.get('img5')
					i.save()

			redirecion = redirect(reverse('denuncia'))
			return redirecion

	return render(request,'core/create-denuncia.html',{'form':form,'form2':form2})



def CreatePostInfor(request):
	if request.user.is_authenticated:
		usuario = User.objects.get(email = request.user)

		if request.method == 'GET':
			form = CreatePostInformativo()
			form2 = ImagenForm()
		else:
			form = CreatePostInformativo(request.POST)
			form2 = ImagenForm(request.POST, request.FILES)
			if form.is_valid() and form2.is_valid():
				d = form.save(commit = False)
				
				d.created_by = usuario
				d.titulo = request.POST.get('titulo')
				d.text = request.POST.get('text')
				d.post_type = 'INFORATIVO'
				d.save()

				info = PostInformativo.objects.get(pk = d.pk)
				if request.POST.get('img') != '':
					i = form2.save(commit = False)
					i.post = info
					i.img = request.FILES.get('img')
					i.save()

				if request.POST.get('img2') != '':
					form2 = ImagenForm(request.POST, request.FILES)
					i = form2.save(commit = False)
					i.post = info
					i.img = request.FILES.get('img2')
					i.save()

				if request.POST.get('img3') != '':
					form2 = ImagenForm(request.POST, request.FILES)
					i = form2.save(commit = False)
					i.post = info
					i.img = request.FILES.get('img3')
					i.save()

				if request.POST.get('img4') != '':
					form2 = ImagenForm(request.POST, request.FILES)
					i = form2.save(commit = False)
					i.post = info
					i.img = request.FILES.get('img4')
					i.save()

				if request.POST.get('img5') != '':
					form2 = ImagenForm(request.POST, request.FILES)
					i = form2.save(commit = False)
					i.post = info
					i.img = request.FILES.get('img5')
					i.save()

			redirecion = redirect(reverse('informacion'))
			return redirecion

	else:

		redirecion = redirect(reverse('usuario:register'))
		return redirecion

	return render(request,'core/create-info.html',{'form':form,'form2':form2})



def listar(request):
	context = {}
	de = Denuncia.objects.order_by('-creation_date')
	lp = PostInformativo.objects.order_by('-creation_date')
	p = Tree.objects.get(pk=1)
	img = PostImg.objects.distinct('post_id')
	context['arbol'] = p
	context['denuncias'] = de
	context['informativo'] = lp
	context['imagen'] = img

	return render(request, 'core/home.html', context)


def ListarPostDenuncia(request):
	context = {}
	objdenuncia = Denuncia.objects.order_by('-creation_date')
	p = Tree.objects.get(pk=1)
	img = PostImg.objects.distinct('post_id')
	context['denuncias'] = objdenuncia
	context['imagen'] = img

	return render(request, 'core/denuncias.html', context)


def ListPostInformativo(request):

	context = {}

	objeInfo = PostInformativo.objects.order_by('-creation_date')
	p = Tree.objects.get(pk=1)
	img = PostImg.objects.distinct('post_id')
	context['arbol'] = p
	context['info'] = objeInfo
	context['imagen'] = img

	return render(request,'core/informativo.html', context)


# ACA HAY QUE AVERIGUAR COMO HACER PARA ENVIAR EL NUMERO TOTAL DE ARBOLES


class ListPostEventos(ListView):
	pass

