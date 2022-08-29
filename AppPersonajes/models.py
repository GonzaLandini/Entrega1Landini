from django.db import models

# Create your models here.

class PersonajePrincipal(models.Model):
    nombre=models.CharField(max_length=50)
    genero=models.CharField(max_length=50)
    raza=models.CharField(max_length=50)
    altura=models.IntegerField()
    peso=models.IntegerField()

    def __str__(self) -> str:
        return self.nombre+", "+self.raza

class Compañero(models.Model):
    nombre=models.CharField(max_length=50)
    genero=models.CharField(max_length=50)
    raza=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre+", "+self.raza

class Ubicacion(models.Model):
    region=models.CharField(max_length=50)
    aldea=models.CharField(max_length=50)
    siglo=models.IntegerField() 

    def __str__(self) -> str:
        return self.region