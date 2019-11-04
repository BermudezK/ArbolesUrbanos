from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #url principal
    path('admin/', admin.site.urls),

    #URL REDIRECCIONAR
    path('arbol/', include('apps.arbol.urls')),

    # urls de post
    path('post/', include('apps.post.urls')),
    
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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
