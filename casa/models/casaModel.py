from django.db import models

class Casa(models.Model):
    numero = models.IntegerField()
    foto = models.BinaryField(editable=True)
    cemento = models.DecimalField(max_digits=10, decimal_places=2,default=0.0)
    ladrillo = models.DecimalField(max_digits=10, decimal_places=2,default=0.0)

    def __str__(self):
        return str(self.numero)