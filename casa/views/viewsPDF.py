from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from casa.models.casaModel import Casa
import io
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

def some_view(request):
    buffer = io.BytesIO()

    # Crea el PDF
    doc = SimpleDocTemplate(buffer, pagesize=letter)

    # Contenedor para los elementos del 'Flowable'
    elements = []

    # Estilos de párrafo
    styles = getSampleStyleSheet()

    # Agrega algunos elementos de 'Flowable'
    elements.append(Paragraph('Mi Título', styles['Title']))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph('Subtítulo', styles['Heading2']))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph('Texto del informe...', styles['BodyText']))

    # Obtiene la imagen de la base de datos
    image_model = Casa.objects.get(id=1)
    image_data = image_model.foto

    # Crea un ImageReader con los datos de la imagen
    image = ImageReader(io.BytesIO(image_data))

    # Agrega la imagen al PDF
    elements.append(image)

    # Construye el PDF
    doc.build(elements)

    # Crea una respuesta con el archivo PDF
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='somefilename.pdf')