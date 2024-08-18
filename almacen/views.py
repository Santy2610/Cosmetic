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
    alma = almacenb.objects.filter(idinver=inver).order_by('descripcion')
    listado = almacenb.objects.values('descripcion').order_by(
        'descripcion').annotate(sun=Sum('cantidad'))
    formal = almacenf()
    return render(request, "indexal.html", {"almaSW": alma, "formalSW": formal, "inverSW": inver, "invcontSW": dato, "listadoSW": listado, "conal": cantalm})


def almadd(request, dato):
    inv = inversion.objects.get(pk=dato)
    descripc = request.GET["descripcionf"]
    presv = request.GET["presiobf"]
    presc = request.GET["presiocf"]
    cant = request.GET["cantidadf"]
    gana1 = float(presv)-float(presc)
    gana2 = float(presv)*int(cant)
    ganainv = float(presc)*int(cant)

    alma = almacenb.objects.create(
        idinver=inv, descripcion=descripc, presiob=presv, presioc=presc, cantidad=cant, ganancia=gana1, existencia=cant)
    inv.montoganancia = inv.montoganancia+gana2
    inv.montoinver = inv.montoinver+ganainv
    inv.libre = inv.montoganancia-inv.montoinver
    inv.save()
    return redirect("/indexalm/"+dato+"/0")


def almadel(request, dato, id):
    alma = almacenb.objects.get(pk=id)
    inv = inversion.objects.get(pk=dato)
    inv.montoganancia = inv.montoganancia-(alma.presiob*alma.cantidad)
    inv.montoinver = inv.montoinver-(alma.presioc*alma.cantidad)
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
                    'cantidad': alm.cantidad,
                    'existencia': alm.existencia
                })

    # page = request.GET.get('page', 1)
    # paginador = Paginator(resul, 12)
    # resul = paginador.page(page)

    return render(request, "listalmacen.html", {"resultSW": resul, "conal": cantalm})


def indexinv(request, edit, dato):

    invert = inversion.objects.all().order_by('-fecha')

    # fecha1 = datetime.now()
    # yearinv = fecha1.year

    if edit == "edit":
        invsel = inversion.objects.get(pk=dato)
        forminv = inversionf(
            initial={'fechaf': invsel.fecha,  'montoinvf': invsel.montoinver})
        edit = "edit"
        return render(request, "indexinv.html", {"formSW": forminv, "invertSW": invert, "editSW": edit, "datoSW": dato, "invuSW": invsel,  "conal": cantalm})
    elif edit == "add":
        forminv = inversionf()
        edit = "add"
        return render(request, "indexinv.html", {"formSW": forminv, "invertSW": invert, "editSW": edit, "datoSW": dato,  "conal": cantalm})
    else:
        forminv = inversionf()
        edit = "noedit"
        return render(request, "indexinv.html", {"formSW": forminv, "invertSW": invert, "editSW": edit, "datoSW": dato, "conal": cantalm})


def invadd(request):
    fecha = request.GET["fechaf"]
    montoinv = 0
    montogan = 0
    libreinv = 0
    fechar = datetime.strptime(fecha, "%Y-%m-%d")
    mesinv = fechar.month
    inv = inversion.objects.create(
        fecha=fecha, mes=mesinv, montoinver=montoinv, montoganancia=montogan, libre=libreinv)
    return redirect("/indexinv/index/0")


def invupdate(request, dato):
    fecha = request.GET["fechaf"]
    fechar = datetime.strptime(fecha, "%Y-%m-%d")
    mesinv = fechar.month
    inv = inversion.objects.get(pk=dato)
    inv.fecha = fecha
    inv.mes = mesinv
    inv.save()
    return redirect("/indexinv/index/0")


def invdell(request, dato):
    inv = inversion.objects.get(pk=dato)
    inv.delete()
    return redirect("/indexinv/index/0")


def cal(request):
    alm = almacenb.objects.all()
    for alm in alm:
        alm.ganancia = alm.presiob-alm.presioc
        alm.save()
    return redirect("/indexinv/index/0")


def invt(request):
    alm = almacenb.objects.all()
    tot = 0
    tot2 = 0
    for alm in alm:
        tot = tot+(alm.presioc*alm.cantidad)
        tot2 = tot2+(alm.presiob*alm.cantidad)
    inv = inversion.objects.get(pk=1)
    inv.montoinver = tot
    inv.montoganancia = tot2
    inv.libre = inv.montoganancia-inv.montoinver
    inv.save()
    return redirect("/indexinv/index/0")
