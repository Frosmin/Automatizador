from django.http import FileResponse
from casa.models.casaModel import Casa
import io
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
import lorem

def some_view(request):
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
    
    
    
    text = Paragraph(lore, styles['BodyText'])
    elements.append(text)

    # Espacio
    elements.append(Spacer(1, 12))

    # Imagen
    image_model = Casa.objects.get(id=1)
    image_path = image_model.foto
    image = Image(io.BytesIO(image_path), 200, 200)
    elements.append(image)

    # Genera el PDF
    doc.build(elements)

    # Crea una respuesta con el archivo PDF
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='informe.pdf')