from django.shortcuts import render
from Proveedores.forms import Proveedoresform

# Create your views here.

def index(request):
    return render(request, 'Base.html')

def Proveedoresview(request):
    form = Proveedoresform()

    return render(request, 'Proveedores.html',{'form':form})

def Consultarviews(request):
    return render (request, 'Consultas.html')