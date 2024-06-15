from django.db import models

class Casa(models.Model):
    numero = models.IntegerField()
    foto = models.BinaryField(editable=True)

    def __str__(self):
        return str(self.numero)