from django.shortcuts import render
from .models import Service

# Create your views here.
def services(request):
    servicios = Service.objects.all()
    contexto = {"servicios":servicios}
    return render(request, template_name='services/services.html', context=contexto)