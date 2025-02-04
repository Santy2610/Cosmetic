from django.db import models

# Create your models here.


class venta(models.Model):
    fecha = models.DateField()
    descripcion = models.CharField(max_length=150)
    cantidad = models.IntegerField()
    ganancia = models.FloatField()
    presioc = models.FloatField()
    idalma = models.IntegerField()


class pedido(models.Model):
    descripcion = models.CharField(max_length=150)
    cantidad = models.IntegerField()


class promot(models.Model):
    nombre = models.CharField(max_length=255)


class articulo(models.Model):
    idNombre = models.ForeignKey(
        promot, on_delete=models.CASCADE, null=False, blank=False)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=150)
    cantidad = models.IntegerField()
