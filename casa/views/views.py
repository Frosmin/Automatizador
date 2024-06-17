
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from ..forms import CasaForm
from casa.models.casaModel import Casa
from django.contrib import messages
from django.core.exceptions import ValidationError
import base64
from django.http import Http404
from django.http import FileResponse
from reportlab.pdfgen import canvas
import io


# Create your views here.
def home(request):
    casa = Casa.objects.last()  # obtiene la última casa añadida
    return render(request, 'home.html', {'casa': casa})

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
        numero = request.POST['numero']
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
    return render(request, 'upload.html')


def mostrar_foto(request):
    numero = request.GET.get('numero')
    casa = Casa.objects.filter(numero=numero).first()

    if not casa:
        raise Http404("Casa no encontrada")

    # Convertir la imagen a base64
    foto_base64 = base64.b64encode(casa.foto).decode('utf-8')

    return render(request, 'home.html', {'casa': casa, 'foto_base64': foto_base64})


# def some_view(request):
#     # Crea un archivo PDF en la memoria
#     buffer = io.BytesIO()
#     p = canvas.Canvas(buffer)

#     # Aquí va el código para generar tu PDF...

#     p.showPage()
#     p.save()

#     # Crea una respuesta con el archivo PDF
#     buffer.seek(0)
#     return FileResponse(buffer, as_attachment=True, filename='nombre_del_archivo.pdf')