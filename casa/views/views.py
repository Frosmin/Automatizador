
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from casa.models.casaModel import Casa
from django.core.exceptions import ValidationError
import base64
from django.http import Http404
from django import forms



# Create your views here.
def home(request):
    casas = Casa.objects.all()  # Obtiene todas las casas
    return render(request, 'home.html', {'casas': casas})


class CasaForm(forms.Form):
    numero = forms.ModelChoiceField(queryset=Casa.objects.all().order_by('numero'))



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
        numero = request.session.get('numero_casa')
        casas = Casa.objects.all()  # Obtiene todas las casas
        foto_file = request.FILES['foto']

        # Validar que el archivo es una imagen
        if not foto_file.content_type.startswith('image/'):
            raise ValidationError('El archivo cargado no es una imagen')

        # Leer el archivo en chunks para evitar problemas de memoria
        foto = b''
        for chunk in foto_file.chunks():
            foto += chunk

        casa = Casa(numero=numero, foto=foto)
        casa.save()
    return render(request, 'upload.html',{'casas': casas})


def mostrar_foto(request):
    numero = request.session.get('numero_casa')
    casa = Casa.objects.filter(numero=numero).first()
    casas = Casa.objects.all()  # Obtiene todas las casas

    if not casa:
        raise Http404("Casa no encontrada")

    # Convertir la imagen a base64
    foto_base64 = base64.b64encode(casa.foto).decode('utf-8')

    return render(request, 'home.html', {'casas': casas,'casa': casa, 'foto_base64': foto_base64})



#buenos  Subir
def subir_cemento(request):
    if request.method == 'POST':
        numero = request.session.get('numero_casa')   #numerp de la secion :D
        cemento = request.POST['cemento']
        casas = Casa.objects.all()  # Obtiene todas las casas
        
        casa = Casa.objects.filter(numero=numero).first()
        
        if not casa:
            raise Http404("Casa no encontrada")
        
        casa.cemento = cemento
        casa.save()
    return render(request,'home.html', {'casas': casas})


def subir_ladrillo(request):
    if request.method == 'POST':
        numero = request.session.get('numero_casa')   #numerp de la secion :D
        ladrillo_nuevo = request.POST['ladriillo']
        casas = Casa.objects.all()  # Obtiene todas las casas
        
        casa = Casa.objects.filter(numero=numero).first()
        
        if not casa:
            raise Http404("Casa no encontrada")
        
        casa.ladrillo = ladrillo_nuevo
        casa.save()
    return render(request,'home.html',{casas: casas})


def seleccionar_casa(request):
    if request.method == 'POST':
        numero = request.POST['numero']
        request.session['numero_casa'] = numero
    casas = Casa.objects.all()  # Obtiene todas las casas
    return render(request, 'home.html', {'casas': casas})







def mostrar(request):
    if request.method == 'POST':
        casas = Casa.objects.all()  # Obtiene todas las casas
        numeros_de_casas = Casa.objects.all().values_list('numero', flat=True)
        return render(request, 'home.html', {'numeros_de_casas': numeros_de_casas, 'casas': casas})
        
    else:
        return render(request, 'home.html',{'casas': casas})