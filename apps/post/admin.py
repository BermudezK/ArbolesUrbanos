# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . models import Denuncia, PostInformativo, PostImg



admin.site.register(Denuncia)
admin.site.register(PostInformativo)
admin.site.register(PostImg)
