from django.shortcuts import render, redirect
from almacen.models import almacenb, inversion
from almacen.formulario import inversionf
from datetime import datetime

# Create your views here.


def indexalm(request):
    return render(request, "indexal.html")


def indexinv(request):
    forminv = inversionf()
    invert = inversion.objects.all()
    fecha1 = datetime.now()
    yearinv = fecha1.year
    return render(request, "indexinv.html", {"formSW": forminv, "invertSW": invert, "yearSW": yearinv})


def invadd(request):
    fecha = request.GET["fechaf"]
    montoinv = request.GET["montoinvf"]
    montogan = 0
    libreinv = 0
    fechar = datetime.strptime(fecha, "%Y-%m-%d")
    mesinv = fechar.month
    inv = inversion.objects.create(
        fecha=fecha, mes=mesinv, montoinver=montoinv, montoganancia=montogan, libre=libreinv)
    return redirect(indexinv)


def invupdate(request, dato):
    fecha = request.GET["fechaf"]
    montoinv = request.GET["montoinvf"]


def invdell(request, dato):
    inv = inversion.objects.get(pk=dato)
    inv.delete()
    return redirect(indexinv)
