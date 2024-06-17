from django.http import FileResponse
from reportlab.pdfgen import canvas

def some_view(request):
    # Crea un objeto de archivo PDF
    response = FileResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # Crea el PDF
    p = canvas.Canvas(response)

    # Dibuja cosas en el PDF. Aquí es donde se genera el contenido.
    # Consulta la documentación de reportlab para ver las opciones completas
    p.drawString(100, 100, "Hello world.")

    # Cierra el objeto PDF limpiamente.
    p.showPage()
    p.save()
    return response