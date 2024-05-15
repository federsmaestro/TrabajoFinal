from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from . import models, forms

def index(request):
   
    return render(request,"Empresa/index.html")

class EmpresaList(ListView):
    model = models.Empresa

class EmpresaCreate(CreateView):
    model = models.Empresa
    form_class=forms.EmpresaForm
    success_url = reverse_lazy("Empresa:empresa_list")