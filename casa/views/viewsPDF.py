from django.http import FileResponse ,HttpResponse
from casa.models.casaModel import Casa
import io
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
import lorem
from django.http import FileResponse
from casa.models.casaModel import Casa
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def some_view(request):
    
    
    if request.method == 'POST':
        numero_casa = request.POST.get('numero')
        return redirect('some_view')
    else:
        numero_casa = request.session.get('numero_casa', None)
        if numero_casa is None:
            return HttpResponse('No se proporcionó un número de casa')
        casa = Casa.objects.filter(numero=numero_casa).first()
        if casa is None:
            return HttpResponse('No existe una casa con ese número')

        
        
        
        # Crea un objeto de archivo PDF en memoria
        buffer = io.BytesIO()
        # Crea el PDF
        doc = SimpleDocTemplate(buffer, pagesize=letter)

        # Contenido del PDF
        elements = []

        # Estilos
        styles = getSampleStyleSheet()

        # Título
        title = Paragraph("Título del Informe", styles['Title'])
        elements.append(title)

        # Espacio
        elements.append(Spacer(1, 12))

        # Subtítulo
        subtitle = Paragraph("Subtítulo del Informe", styles['Heading2'])
        elements.append(subtitle)

        # Espacio
        
        elements.append(Spacer(1, 12))

        lore = lorem.text()+ lorem.text()+lorem.text()+ lorem.text()+lorem.text()+ lorem.text()+lorem.text()+ lorem.text()+lorem.text()+ lorem.text()
        # Texto
        # text = Paragraph("""Aquí va el texto del informe..               
        #                  """, styles['BodyText'])
        
        
        
        text = Paragraph(lore, styles['BodyText']) ##texto de prueba 
        elements.append(text)

        # Espacio
        elements.append(Spacer(1, 12))

        # Imagen
        try:
              image_model = casa
        except Casa.DoesNotExist:
            return HttpResponse('Casa no encontrada')
        image_path = image_model.foto
        image = Image(io.BytesIO(image_path), 200, 200)
        elements.append(image)

        # Genera el PDF
        doc.build(elements)

        # Crea una respuesta con el archivo PDF
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename='informe.pdf')