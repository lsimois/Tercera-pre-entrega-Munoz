from django.db import models

# Create your models here.

class Juegos_de_Mesa(models.Model):
    codigo = models.IntegerField()
    nombre= models.CharField(max_length=50)
    cant_jugadores = models.CharField(max_length=50)
    edad_recomendada = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=9, decimal_places=2)

class Miniaturas(models.Model):
    codigo = models.IntegerField()
    nombre= models.CharField(max_length=50)
    escala = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=9, decimal_places=2)

class Libros(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    cant_pag = models.IntegerField()
    precio = models.DecimalField(max_digits=9, decimal_places=2)