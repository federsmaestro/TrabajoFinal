from django.urls import path

from . import views

app_name = "Empresa"

urlpatterns = [
    
    path('', views.index, name= "index"),                 
    path('empresa/list', views.EmpresaList.as_view(), name= "empresa_list"),                 
    path('empresa/create', views.EmpresaCreate.as_view(), name= "empresa_create"),                 
    path("empresa/detail/<int:pk>", views.EmpresaDetail.as_view(), name="empresa_detail"),
    path("empresa/delete/<int:pk>", views.EmpresaDelete.as_view(), name="empresa_delete"),
    
]