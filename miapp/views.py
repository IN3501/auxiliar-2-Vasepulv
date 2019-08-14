from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def pestaña(request):
    return render(request, 'pestaña.html')

def integrantes(request):
    return render(request, 'integrantes.html')
