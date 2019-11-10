# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .forms import CreateDenuncia, CreatePostInformativo
from .models import Denuncia, PostInformativo

class CreateDenuncia(CreateView):
	form_class = CreateDenuncia
	template_name = 'core/create-denuncia.html'
	success_url = reverse_lazy('denuncia-home')

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.created_by = self.request.user
		return super(CreateDenuncia, self).form_valid(form)

class CreatePostInformativo(CreateView):
	form_class = CreatePostInformativo
	template_name = 'core/create-info.html'
	success_utl = reverse_lazy('home')

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.created_by = self.request.user
		return super(CreatePostInformativo, self).form_valid(form)


def listar(request):
	context = {}
	de = Denuncia.objects.order_by('-creation_date')
	lp = PostInformativo.objects.order_by('-creation_date')

	context['denuncias'] = de
	context['informativo'] = lp

	return render(request, 'core/home.html', context)



class ListPostDenuncia(ListView):
	model = Denuncia
	template_name = 'core/denuncias.html'

	def get_queryset(self):
		result = Denuncia.objects.order_by('-creation_date')
		return result

class ListPostInformativo(ListView):
	model = PostInformativo
	template_name = 'core/informativo.html'

	def get_queryset(self):
		result = PostInformativo.objects.order_by('-creation_date')
		return result

class ListPostEventos(ListView):
	pass



	