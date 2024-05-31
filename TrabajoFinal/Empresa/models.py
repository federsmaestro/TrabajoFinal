from django.db import models

# Create your models here.

class Sector(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.nombre


class Industria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nombre


class Pais(models.Model):
    nombre = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)

    def __str__(self) -> str:
        return self.nombre


class Empresa(models.Model):
    nombre = models.CharField(unique=True,max_length=50)
    sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True, blank=True)
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)
    industria = models.ForeignKey(Industria, on_delete=models.SET_NULL, null=True, blank=True)