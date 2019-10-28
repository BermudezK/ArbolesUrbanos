"""arbolesurbanos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as view

urlpatterns = [
    #url principal
    path('admin/', admin.site.urls),

    #URL REDIRECCIONAR
    path('arbol/', include('apps.arbol.urls')),
    #urls de core
    path('', include('apps.core.urls')),

    #url de usuario
    path('register/', include('apps.usuario.urls')),
    
    #url Login
    path('login/', view.LoginView.as_view(template_name = 'registration/login.html'), name = 'login'),
    path('logout', view.LogoutView.as_view(), name="logout"),

    #url Password
    path('accounts/', include('django.contrib.auth.urls')),
    re_path('accounts/reset/<uidb64>/<token>/',view.PasswordResetConfirmView.as_view(template_name = 'registration/password_reset_confirm.html'), name='password_reset_confirm'),
]
