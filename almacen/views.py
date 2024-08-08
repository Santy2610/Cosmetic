from django.shortcuts import render, redirect
from almacen.models import almacenb, inversion
from almacen.formulario import inversionf, almacenf
from datetime import datetime
from django.core.paginator import Paginator
from django.db.models import Sum
from cosmetic.views import cantalm

# Create your views here.


def indexalm(request, dato, valor):
    inver = inversion.objects.get(pk=dato)
    page = request.GET.get('page', 1)
    alma = almacenb.objects.filter(idinver=inver).order_by('descripcion')
    paginador = Paginator(alma, 7)
    alma = paginador.page(page)
    listado = almacenb.objects.values('descripcion').order_by(
        'descripcion').annotate(sun=Sum('cantidad'))
    formal = almacenf()
    return render(request, "indexal.html", {"almaSW": alma, "formalSW": formal, "inverSW": inver, "paginador": paginador, "listpsw": alma, "invcontSW": dato, "listadoSW": listado, "conal": cantalm})


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
    return redirect("/indexalm/"+dato+"/0")


def almadel(request, dato, id):
    alma = almacenb.objects.get(pk=id)
    inv = inversion.objects.get(pk=dato)
    inv.montoganancia = inv.montoganancia-alma.ganancia
    inv.libre = inv.montoganancia-inv.montoinver
    inv.save()
    alma.delete()
    return redirect("/indexalm/"+dato+"/0")


def listalmacen(request):
    resul = []
    inv = inversion.objects.all().order_by('fecha')
    for inv in inv:
        alm = almacenb.objects.filter(
            idinver=inv).order_by('descripcion')
        for alm in alm:
            if alm.existencia > 0:
                resul.append({
                    'fecha': inv.fecha,
                    'descripcion': alm.descripcion,
                    'existencia': alm.existencia
                })

    page = request.GET.get('page', 1)
    paginador = Paginator(resul, 12)
    resul = paginador.page(page)

    return render(request, "listalmacen.html", {"resultSW": resul, "paginador": paginador, "listpsw": resul, "conal": cantalm})


def indexinv(request, edit, dato):

    page = request.GET.get('page', 1)
    invert = inversion.objects.all().order_by('fecha')
    paginador = Paginator(invert, 10)
    invert = paginador.page(page)

    # fecha1 = datetime.now()
    # yearinv = fecha1.year

    if edit == "edit":
        invsel = inversion.objects.get(pk=dato)
        forminv = inversionf(
            initial={'fechaf': invsel.fecha,  'montoinvf': invsel.montoinver})
        edit = "edit"
        return render(request, "indexinv.html", {"formSW": forminv, "invertSW": invert, "editSW": edit, "datoSW": dato, "invuSW": invsel, "paginador": paginador, "listpsw": invert, "conal": cantalm})
    elif edit == "add":
        forminv = inversionf()
        edit = "add"
        return render(request, "indexinv.html", {"formSW": forminv, "invertSW": invert, "editSW": edit, "datoSW": dato, "paginador": paginador, "listpsw": invert, "conal": cantalm})
    else:
        forminv = inversionf()
        edit = "noedit"
        return render(request, "indexinv.html", {"formSW": forminv, "invertSW": invert, "editSW": edit, "datoSW": dato, "paginador": paginador, "listpsw": invert, "conal": cantalm})


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
