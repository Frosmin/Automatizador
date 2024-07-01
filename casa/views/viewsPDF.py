from django.http import FileResponse ,HttpResponse
from casa.models.casaModel import Casa
import io
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
import lorem
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors

@csrf_exempt
def some_view(request):
    
    
    if request.method == 'POST':
        casas = Casa.objects.all()  # Obtiene todas las casas
        numero_casa = request.POST.get('numero')
        return redirect('some_view')
        
    else:
        numero_casa = request.session.get('numero_casa', None)
        if numero_casa is None:
            return HttpResponse('No se proporcionó un número de casa')
        casa = Casa.objects.filter(numero=numero_casa).first()
        if casa is None:
            return HttpResponse('No existe una casa con ese número')

       #revisar
        ladrillo = casa.Ladrillo.objects.filter(numero=numero_casa).first()
                
        
        
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

        # lore = lorem.text()+ lorem.text()+lorem.text()+ lorem.text()+lorem.text()+ lorem.text()+lorem.text()+ lorem.text()+lorem.text()+ lorem.text()
        
        
        # Texto
        text1 = Paragraph("""Aquí va el texto del informe..    
                         
                         
                                    
                         """, styles['BodyText'])
        elements.append(text1)
        
        
        # Datos de la tabla
        data = [
            [ladrillo, 'Header 2', 'Header 3'],  # Encabezados
            ['Row 1', 'Example 1', 'Example 2'],   # Primera fila
            ['Row 2', 'Example 3', 'Example 4'],   # Segunda fila
            # Añade más filas según sea necesario
        ]
        
                # Crea la tabla
        table = Table(data)

        # Estilo de la tabla
        table_style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Color de fondo para los encabezados
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Color del texto para los encabezados
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Alineación del texto
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Fuente de los encabezados
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Padding inferior para los encabezados
            ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Bordes de la tabla
            # Añade más estilos según sea necesario
        ])
        
        table.setStyle(table_style)
        elements.append(table)
        
        #sirve para loreipsum
        # texto = Paragraph(text1, styles['BodyText']) ##texto de prueba 
        # elements.append(texto)

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