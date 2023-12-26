from django.db import models
from django import forms
from django.utils import timezone

class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Prenda(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Evento(models.Model):
    TIPOS_EVENTO = [
        ('lanzamiento', 'Nuevo Lanzamiento'),
        ('fiesta', 'Fiesta'),
        ('apertura_tienda', 'Apertura de Tienda'),
        ('descuentos', 'Descuentos Especiales'),
        # Puedes agregar más opciones según sea necesario
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100, choices=TIPOS_EVENTO)
    fecha = models.DateField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

   