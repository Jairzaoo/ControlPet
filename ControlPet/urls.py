from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.contrib.auth.decorators import login_required
from ControlPetApp import views  # Import your views from the app

urlpatterns = [
    path('temperatura/', views.temperatura, name='temperatura'),
    path('', views.index, name='index'),  # Página inicial
    path('login/', views.login, name='login'),
    path('', views.index, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('consulta/', views.consulta, name='consulta'),
    path('editarpet/<int:pet_id>/', views.editar_pet, name='editar_pet'),
    path('deletarpet/<int:pet_id>/', views.deletar_pet, name='deletar_pet'),
    path('cadastrarpet/', login_required(views.cadastrar_pet), name='cadastrar_pet'),
    path('marcarconsulta/<int:pet_id>/', views.marcar_consulta, name='marcar_consulta'),
    path('get_available_times/', views.get_available_times, name='get_available_times'),  # New URL pattern
]