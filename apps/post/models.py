# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from .utils import TipoDenunciaEnum, TipoPostEnum
from apps.usuario.models import User

class PostBase(models.Model):
	created_by = models.ForeignKey(User, on_delete=models.CASCADE)
	img = models.ImageField(blank=True, null=True)
	creation_date = models.DateTimeField(auto_now_add=True)
	post_type = models.CharField(choices=TipoPostEnum.choices(), max_length=25)


class Denuncia(PostBase):
	tipo = models.CharField(choices=TipoDenunciaEnum.choices(), max_length=25)
	text = models.CharField(max_length=500)


class PostInformativo(PostBase):
	text = models.CharField(max_length=1000)




