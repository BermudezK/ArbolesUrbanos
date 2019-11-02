# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from apps.usuario.models import User

class Post(models.Models):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	img = models.ImageField(blank=True, null=True)
	date_time = models.DateTimeField(auto_now_add=True)
	


