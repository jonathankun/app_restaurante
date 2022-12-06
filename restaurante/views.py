from django.shortcuts import render
from restaurante.models import Mesero
from restaurante.models import Plato

from django.db.models import F
from django.db.models import Q

# Create your views here.
def mesero_list(request):

    meseros = Mesero.objects.all()
    return render(request, 'mesero/mesero_list.html', context={'data': meseros})


def plato_list(request):

    platos = Plato.objects.all()
    return render(request, 'plato/plato_list.html', context={'data': platos})


def platillo_query(request):
    platos = Plato.objects.all()
    """Primer Plato agregado"""
    p = Plato(nombre="Tacu Tacu",precio=55, procedencia="Perú")
    p.save()
    """Segundo Plato agregado"""
    p = Plato(nombre="Carapulcra", precio=25, procedencia="Perú")
    p.save()
    """Tercer Plato agregado"""
    p = Plato(nombre="Ceviche", precio=45, procedencia="Perú")
    p.save()

    platos = Plato.objects.filter(procedencia="Perú", precio__gt=40)

    return render(request, 'plato/plato_list.html', context={'data': platos})

def mesero_query(request):
    meseros = Mesero.objects.all()
    meseros = Mesero.objects.filter(procedencia="Perú", edad__lt=30)
    return render(request, 'mesero/mesero_list.html', context={'data': meseros})

def mesero_query2(request):
    Mesero.objects.filter().update(edad=F('edad') + 5)
    meseros = Mesero.objects.all()
    return render(request, 'mesero/mesero_list.html', context={'data': meseros})