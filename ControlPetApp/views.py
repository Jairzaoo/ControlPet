from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import authenticate, login as auth_login, logout
from .decorators import login_redirect

def index(request):
    return render(request, 'index.html')


def login(request):
    if request.user.is_authenticated:  # Check if user is already logged in
        return redirect('consulta')  # Redirect to consulta if logged in

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('consulta')  # Redirect to consulta after successful login
            else:
                messages.error(request, 'Email ou senha inválido.')
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})

@login_redirect
def consulta(request):
    return render(request, 'consulta.html')
    
    

def cadastro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro completo! Faça login para acessar sua conta.')
            return redirect('login')  
    else:
        form = UserRegisterForm()

    return render(request, 'cadastro.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')