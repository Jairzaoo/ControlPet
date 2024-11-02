from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import authenticate, login as auth_login, logout
from .decorators import login_redirect
from .models import Pet
from datetime import datetime, time, timedelta
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'index.html')

def temperatura(request):
    return render(request, 'temperatura.html')

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
    pets = Pet.objects.filter(owner=request.user)
    return render(request, 'consulta.html', {'pets': pets})

def deletar_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id, owner=request.user)
    pet.delete()
    messages.success(request, 'Pet deletado com sucesso!')
    return redirect('consulta')

def editar_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id, owner=request.user)
    if request.method == 'POST':
        pet.name = request.POST['pet_name']
        pet.pet_type = request.POST['pet_type']
        pet.consultation_date = request.POST['consultation_date']
        pet.vaccine = request.POST['vaccine']
        pet.last_vaccine_date = request.POST['last_vaccine_date'] if pet.vaccine != 'Não Vacinado' else None
        pet.save()
        messages.success(request, 'Pet atualizado com sucesso!')
        return redirect('consulta')
    return render(request, 'editarpet.html', {'pet': pet})

def cadastrar_pet(request):
    if request.method == 'POST':
        pet_name = request.POST['pet_name']
        pet_type = request.POST['pet_type']
        vaccine = request.POST['vaccine']
        last_vaccine_date = request.POST['last_vaccine_date'] if vaccine != 'Não Vacinado' else None

        # Save the pet linked to the logged-in user
        pet = Pet(
            name=pet_name,
            pet_type=pet_type,
            owner=request.user,
            last_vaccine_date=last_vaccine_date,
            vaccine=vaccine
        )
        pet.save()

        messages.success(request, 'Pet cadastrado com sucesso!')
    
    return render(request, 'cadastrarpet.html')

def marcar_consulta(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id, owner=request.user)
    if request.method == 'POST':
        consultation_date = request.POST['consultation_date']
        consultation_time = request.POST['consultation_time']
        
        # Combine date and time into a single datetime object
        consultation_datetime_str = f"{consultation_date} {consultation_time}"
        consultation_datetime = datetime.strptime(consultation_datetime_str, '%Y-%m-%d %H:%M')

        # Check if the date is a weekend
        if consultation_datetime.weekday() >= 5:  # 5 = Saturday, 6 = Sunday
            messages.error(request, 'Consultas não podem ser marcadas aos finais de semana.')
            return render(request, 'marcarconsulta.html', {'pet': pet})

        # Check if the time is within work hours (8 AM to 6 PM)
        if not (time(8, 0) <= consultation_datetime.time() <= time(18, 0)):
            messages.error(request, 'Consultas só podem ser marcadas das 8h às 18h.')
            return render(request, 'marcarconsulta.html', {'pet': pet})

        # Save the combined datetime to the pet's consultation_date field
        pet.consultation_date = consultation_datetime.date()
        pet.consultation_time = consultation_datetime.time()
        pet.save()
        messages.success(request, 'Consulta marcada com sucesso!')
        return redirect('consulta')
    return render(request, 'marcarconsulta.html', {'pet': pet})

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

@csrf_exempt
def get_available_times(request):
    if request.method == 'POST':
        consultation_date = request.POST.get('consultation_date')  # Get date from POST
        print(f"Received consultation_date: {consultation_date}")
        
        if consultation_date:
            try:
                # Parse the date string to a date object
                consultation_date = datetime.strptime(consultation_date, '%Y-%m-%d').date()
                print(f"Parsed consultation_date: {consultation_date}")
                
                # Fetch appointments for the specific consultation date
                appointments = Pet.objects.filter(consultation_date=consultation_date)
                print(f"Found appointments: {appointments}")
                
                # Get the consultation times
                booked_times = {appointment.consultation_time for appointment in appointments if appointment.consultation_time}
                print(f"Booked times: {booked_times}")
                
                # Generate the available time slots
                startTime = time(8, 0)  # 8:00 AM
                endTime = time(18, 0)  # 6:00 PM
                interval = timedelta(minutes=30)

                available_times = []
                current_time = datetime.combine(consultation_date, startTime)
                end_time = datetime.combine(consultation_date, endTime)

                while current_time <= end_time:
                    current_time_str = current_time.strftime('%H:%M')
                    if current_time.time() not in booked_times:
                        available_times.append(current_time_str)
                    current_time += interval

                return JsonResponse({'available_times': available_times})
            except ValueError as e:
                print(f"Error parsing date: {e}")
                return JsonResponse({'error': 'Invalid date format'}, status=400)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)