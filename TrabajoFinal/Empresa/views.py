from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView
from . import models, forms
from Empresa.models import Empresa
from typing import Any


def index(request):
   
    return render(request,"Empresa/index.html")

class EmpresaList(ListView):
    model = models.Empresa

    def get_queryset(self) -> QuerySet[Any]:
        if self.request.GET.get("busqueda"):
            busqueda =  self.request.GET.get("busqueda")
            consulta = Empresa.objects.filter(nombre__icontains=busqueda)
        else:
            consulta = Empresa.objects.all()

        return consulta

class EmpresaCreate(CreateView):
    model = models.Empresa
    form_class=forms.EmpresaForm
    success_url = reverse_lazy("Empresa:empresa_list")

class EmpresaDetail(DetailView):
    model = Empresa

class EmpresaDelete(DeleteView):
    model = Empresa
