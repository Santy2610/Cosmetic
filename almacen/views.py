from django.shortcuts import render, redirect
from almacen.models import almacenb, inversion
from almacen.formulario import inversionf, almacenf
from datetime import datetime
from django.core.paginator import Paginator

# Create your views here.


def indexalm(request, edit, dato, valor):
    inver = inversion.objects.get(pk=dato)
    page = request.GET.get('page', 1)
    alma = almacenb.objects.filter(idinver=inver).order_by('descripcion')
    paginador = Paginator(alma, 6)
    alma = paginador.page(page)

    if edit == "edit":
        almaf = almacenb.objects.get(pk=valor)
        formal = almacenf(initial={'descripcionf': almaf.descripcion,
                          'presiocf': almaf.presioc, 'presiobf': almaf.presiob, 'cantidadf': almaf.cantidad})
        return render(request, "indexal.html", {"almaSW": alma, "formalSW": formal, "inverSW": inver, "paginador": paginador, "listpsw": alma, "editSW": edit, "invcontSW": dato})
    else:
        formal = almacenf()
        return render(request, "indexal.html", {"almaSW": alma, "formalSW": formal, "inverSW": inver, "paginador": paginador, "listpsw": alma, "editSW": edit, "invcontSW": dato})


def almadd(request, dato):
    inv = inversion.objects.get(pk=dato)
    descripc = request.GET["descripcionf"]
    presv = request.GET["presiobf"]
    presc = request.GET["presiocf"]
    cant = request.GET["cantidadf"]
    gana = float(presv)*int(cant)

    alma = almacenb.objects.create(
        idinver=inv, descripcion=descripc, presiob=presv, presioc=presc, cantidad=cant, ganancia=gana, existencia=cant)
    inv.montoganancia = inv.montoganancia+gana
    inv.libre = inv.montoganancia-inv.montoinver
    inv.save()
    return redirect("/indexalm/noedit/"+dato+"/0")


def almadel(request, dato, id):
    alma = almacenb.objects.get(pk=id)
    inv = inversion.objects.get(pk=dato)
    inv.montoganancia = inv.montoganancia-alma.ganancia
    inv.libre = inv.montoganancia-inv.montoinver
    inv.save()
    alma.delete()
    return redirect("/indexalm/noedit/"+dato+"/0")


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
