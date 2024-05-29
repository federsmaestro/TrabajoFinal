from django.contrib.auth.views import LoginView
from django.shortcuts import render

from .forms import CustomAuthenticationForm


def index(request):
    return render(request, "core/index.html")
# Create your views here.
class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "core/login.html"