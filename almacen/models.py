from django.db import models

# Create your models here.


class inversion(models.Model):
    fecha = models.DateField()
    mes = models.CharField(max_length=2)
    montoinver = models.FloatField()
    montoganancia = models.FloatField()
    libre = models.FloatField()


class almacenb(models.Model):
    idinver = models.ForeignKey(
        inversion, on_delete=models.CASCADE, null=False, blank=False)
    descripcion = models.CharField(max_length=150)
    presioc = models.FloatField()
    presiob = models.FloatField()
    ganancia = models.FloatField()
    cantidad = models.IntegerField()
    existencia = models.IntegerField()
