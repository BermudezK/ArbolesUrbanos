# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .forms import CreateDenuncia, CreatePostInformativo
from .models import Denuncia, PostInformativo

class CreateDenuncia(CreateView):
	form_class = CreateDenuncia
	template_name = 'Post/create-denuncia.html'
	success_url = reverse_lazy('denuncia-home')

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.created_by = self.request.user
		obj.save()
		return HttpResponseRedirect(self.get_success_url())

class CreatePostInformativo(CreateView):
	form_class = CreatePostInformativo
	template_name = 'Post/create-info.html'
	success_utl = reverse_lazy('info-home')

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.created_by = self.request.user
		obj.save()
		return HttpResponseRedirect(self.get_success_url())

class ListDenuncia(ListView):
	model = Denuncia
	template_name = 'Post/listar.html'

class ListPostInformativo(ListView):
	model = PostInformativo
	template_name = 'Post/listar.html'



	