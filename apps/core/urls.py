from django.urls import path, include
from . import views as core_views


urlpatterns = [
    path('', core_views.Inicio, name="home"),
    path('contacto/', core_views.contacto, name="contacto"),
    # path('arbol/', include('apps.arbol.urls')),
    path('landing',core_views.landing,name="landing"),
]

