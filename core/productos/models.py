from django.db import models

# Create your models here.

class Producto(models.Model):
    titulo = models.CharField(max_length = 255, unique = True)
    precio = models.FloatField()
    #detalle = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.titulo
    