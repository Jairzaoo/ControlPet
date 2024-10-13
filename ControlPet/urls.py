from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.contrib.auth.decorators import login_required
from ControlPetApp import views  # Import your views from the app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Página inicial
    path('login/', views.login, name='login'),
    path('', views.index, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('consulta/', views.consulta, name='consulta'), # Import login_required
]
