from django.shortcuts import render

from . import models

def index(request):
    consulta = models.Empresa.objects.all()
    contexto = {"empresas":consulta}
    return render(request,"Empresa/index.html", contexto)

