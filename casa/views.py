
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CasaForm
from casa.models.casaModel import Casa
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  #redirije si es user correcto
        else:
            return render(request, 'login.html', {'error': 'Usuario o contraseña no válidos'})
    else:
        return render(request, 'login.html')

def upload_foto(request):
    if request.method == 'POST':
        form = CasaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Foto subida correctamente.')
            return redirect('home')
    else:
        form = CasaForm()
    return render(request, 'upload.html', {'form': form})