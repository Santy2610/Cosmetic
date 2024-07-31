from django.shortcuts import render, redirect
from almacen.models import almacenb, inversion
from almacen.formulario import inversionf
from datetime import datetime
from django.core.paginator import Paginator

# Create your views here.


def indexalm(request, edit, dato, valor):
    inver = inversion.objects.get(pk=dato)
    page = request.GET.get('page', 1)
    alma = almacenb.objects.filter(idinver=inver).order_by('descripcion')
    paginador = Paginator(alma, 10)
    alma = paginador.page(page)

    if edit == "edit":
        alma = almacenb.objects.filter(
            idinver=inver, pk=valor).order_by('descripcion')
        formal = almacenf(initial={'descripcionf': alma.descripcion,
                          'presiocf': alma.presioc, 'presiobf': alma.presiob, 'cantidadf': alma.cantidad})
        return render(request, "indexal.html", {"almaSW": alma, "formalSW": formal, "inverSW": inver, "paginador": paginador, "listpsw": alma})
    elif edit == "add":
        formal = almacenf()
        return render(request, "indexal.html", {"almaSW": alma, "formalSW": formal, "inverSW": inver, "paginador": paginador, "listpsw": alma})
    else:
        return render(request, "indexal.html", {"almaSW": alma, "inverSW": inver, "paginador": paginador, "listpsw": alma})


def indexalmtot(request):
    inv = inversion.objects.all()
    tot = inversion.almacenb_set
    return render(request, "indexal.html", {"almaSW": tot})


def indexinv(request, edit, dato):

    page = request.GET.get('page', 1)
    invert = inversion.objects.all().order_by('fecha')
    paginador = Paginator(invert, 10)
    invert = paginador.page(page)

    fecha1 = datetime.now()
    yearinv = fecha1.year

    if edit == "edit":
        invsel = inversion.objects.get(pk=dato)
        forminv = inversionf(
            initial={'fechaf': invsel.fecha,  'montoinvf': invsel.montoinver})
        edit = "edit"
        return render(request, "indexinv.html", {"formSW": forminv, "invertSW": invert, "yearSW": yearinv, "editSW": edit, "datoSW": dato, "invuSW": invsel, "paginador": paginador, "listpsw": invert})
    elif edit == "add":
        forminv = inversionf()
        edit = "add"
        return render(request, "indexinv.html", {"formSW": forminv, "invertSW": invert, "yearSW": yearinv, "editSW": edit, "datoSW": dato, "paginador": paginador, "listpsw": invert})
    else:
        forminv = inversionf()
        edit = "noedit"
        return render(request, "indexinv.html", {"formSW": forminv, "invertSW": invert, "yearSW": yearinv, "editSW": edit, "datoSW": dato, "paginador": paginador, "listpsw": invert})


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
