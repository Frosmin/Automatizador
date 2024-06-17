from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from casa.models.casaModel import Casa
import io

def some_view(request):
    # Crea un objeto de archivo PDF en memoria
    buffer = io.BytesIO()

    # Crea el PDF
    p = canvas.Canvas(buffer)

    # Obtiene la imagen de la base de datos
    # Esto es solo un ejemplo, necesitarás ajustarlo a tu modelo y método de obtención de la imagen
    image_model = Casa.objects.get(id=1)
    image_path = image_model.foto

    # Crea un ImageReader con la ruta de la imagen
    image = ImageReader(io.BytesIO(image_path))

    # Dibuja la imagen en el PDF (las coordenadas son x, y, ancho, alto)
    p.drawImage(image, 100, 100, 200, 200)

    p.drawString(100, 100, "Hello world.")
    p.showPage()
    p.save()

    # Crea una respuesta con el archivo PDF
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='somefilename.pdf')