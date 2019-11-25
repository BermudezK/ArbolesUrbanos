# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from .utils import TipoDenunciaEnum, TipoPostEnum
from apps.usuario.models import User

class PostBase(models.Model):
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null = True)
	titulo = models.CharField(max_length=100)
	creation_date = models.DateTimeField(auto_now_add=True)
	post_type = models.CharField(max_length=25)


class Denuncia(PostBase):
	tipo = models.CharField(choices=TipoDenunciaEnum.choices(), max_length=25)
	text = models.TextField(max_length=500)
	email = models.EmailField(max_length=100)


class PostInformativo(PostBase):
	text = models.TextField(max_length=1000)

class PostImg(models.Model):
	nombre = models.CharField(null=True, max_length=25)
	img = models.ImageField(blank=True, null=True)
	post = models.ForeignKey(PostBase, on_delete=models.CASCADE)




