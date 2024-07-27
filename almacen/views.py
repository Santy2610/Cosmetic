from django.shortcuts import render, redirect
from almacen.models import almacenb, inversion
from almacen.formulario import inversionf
from datetime import datetime

# Create your views here.


def indexalm(request, dato):
    inver = inversion.objects.get(pk=dato)
    alma = almacenb.objects.filter(idinver=inver).order_by('descripcion')

    return render(request, "indexal.html", {"almaSW": alma, "inverSW": inver})


def indexalmtot(request):
    inv = inversion.objects.all()
    tot = inversion.almacenb_set
    return render(request, "indexal.html", {"almaSW": tot})


def indexinv(request, edit, dato):
    if edit == "edit":
        invsel = inversion.objects.get(pk=dato)
        forminv = inversionf(
            initial={'fechaf': invsel.fecha,  'montoinvf': invsel.montoinver})
        edit = "edit"
    else:
        forminv = inversionf()
        edit = "noedit"
    invert = inversion.objects.all().order_by('fecha')
    fecha1 = datetime.now()
    yearinv = fecha1.year
    return render(request, "indexinv.html", {"formSW": forminv, "invertSW": invert, "yearSW": yearinv, "editSW": edit, "datoSW": dato})


def invadd(request):
    fecha = request.GET["fechaf"]
    montoinv = request.GET["montoinvf"]
    montogan = 0
    libreinv = 0
    fechar = datetime.strptime(fecha, "%Y-%m-%d")
    mesinv = fechar.month
    inv = inversion.objects.create(
        fecha=fecha, mes=mesinv, montoinver=montoinv, montoganancia=montogan, libre=libreinv)
    return redirect("/indexinv/index/0")


def invupdate(request, dato):
    fecha = request.GET["fechaf"]
    montoinv = request.GET["montoinvf"]
    montogan = 0
    libreinv = 0
    fechar = datetime.strptime(fecha, "%Y-%m-%d")
    mesinv = fechar.month
    inv = inversion.objects.get(pk=dato)
    inv.fecha = fecha
    inv.montoinver = montoinv
    inv.montoganancia = montogan
    inv.libre = libreinv
    inv.mes = mesinv
    inv.save()
    return redirect("/indexinv/index/0")


def invdell(request, dato):
    inv = inversion.objects.get(pk=dato)
    inv.delete()
    return redirect("/indexinv/index/0")
