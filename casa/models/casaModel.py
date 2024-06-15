from django.db import models

class Casa(models.Model):
    numero = models.IntegerField()
    foto = models.ImageField(upload_to='fotos/', editable=True)

    def __str__(self):
        return str(self.numero)