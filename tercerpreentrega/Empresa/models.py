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

    def __str__(self) -> str:
        return self.nombre


class Empresa(models.Model):
    nombre = models.PositiveIntegerField(unique=True)
    sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True, blank=True)
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)
    industria = models.ForeignKey(Industria, on_delete=models.SET_NULL, null=True, blank=True)