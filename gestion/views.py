from django.shortcuts import render, redirect
from cosmetic.views import cantalm
from datetime import date, datetime
from gestion.formulario import vistvent, pedidof
from gestion.models import venta, pedido
from almacen.models import almacenb
from django.db.models import Sum
import locale

# Create your views here.


def indexventa(request):
    sug = 0
    lib = 0
    dat = date.today()
    fechar = request.GET["calef"]
    if fechar == "0000-00-00":
        ven = venta.objects.filter(fecha=dat).values('descripcion', 'idalma').order_by(
            'descripcion').annotate(tot=Sum('cantidad'))
        fechat = dat
        sumga = venta.objects.filter(fecha=dat).order_by('fecha').all()
        for sumga in sumga:
            sug = sug+sumga.ganancia
            lib = lib+(sumga.ganancia-sumga.presioc)
    else:
        fechat = datetime.strptime(fechar, "%Y-%m-%d").date()
        ven = venta.objects.filter(fecha=fechat).values('descripcion', 'idalma').order_by(
            'descripcion').annotate(tot=Sum('cantidad'))
        sumga = venta.objects.filter(fecha=fechat).order_by('fecha').all()
        for sumga in sumga:
            sug = sug+sumga.ganancia
            lib = lib+(sumga.ganancia-sumga.presioc)

    alma = almacenb.objects.filter(existencia__gt=0).order_by('descripcion')
    formc = vistvent(initial={'calef': fechat})
    mes = fechat.month
    dia = fechat.day
    year = fechat.year
    return render(request, "indexventa.html", {"conal": cantalm, "dateSW": fechat, "formSW": formc, "venSW": ven,
                                               "almaSW": alma, "mesSW": mes, "diaSW": dia, "yearSW": year, "sugSW": sug, "libSW": lib})


def addventa(request, fechar, id):
    cantR = request.GET["cant"]
    if cantR != "":
        cant = int(cantR)
        for i in range(cant):
            alma = almacenb.objects.get(pk=id)
            alma.existencia = alma.existencia-1
            ven = venta.objects.create(
                fecha=fechar, descripcion=alma.descripcion, cantidad=1, ganancia=alma.presiob, idalma=alma.id, presioc=alma.presioc)
            alma.save()
            ven.save()
    return redirect("/indexventa?calef="+fechar)


def dismventa(request, fechar, id):
    vent = venta.objects.filter(idalma=id).all()
    for vent in vent:
        loc = vent.id
    tra = venta.objects.get(pk=loc)
    tra.delete()
    alm = almacenb.objects.get(pk=id)
    alm.existencia = alm.existencia+1
    alm.save()
    return redirect("/indexventa?calef="+fechar)


def reportvent(request, date):
    vent = venta.objects.values('fecha').order_by('fecha').annotate(
        sumg=Sum('ganancia'), suml=Sum('presioc'), res=Sum('ganancia')-Sum('presioc'))
    if date == "0":
        las = venta.objects.all().order_by('-fecha')
        for las in las:
            datec = las.fecha
        # date = datetime.strptime(date1, "%Y-%m-%d").date()
        most = venta.objects.values('descripcion').filter(
            fecha=datec).annotate(cant=Sum('cantidad'))
    else:
        locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')
        date = datetime.strptime(date, '%d de %B de %Y').date()
        most = venta.objects.values('descripcion').filter(
            fecha=date).annotate(cant=Sum('cantidad'))
        datec = date
    return render(request, "reportvent.html", {"ventSW": vent, "conal": cantalm, "datecSW": datec, "mostSW": most})


def indexpedid(request):
    formp = pedidof()
    alma = almacenb.objects.filter(existencia=0).values(
        "descripcion").order_by("descripcion")
    pedid = pedido.objects.all()
    return render(request, "indexpedido.html", {"almaSW": alma, "pedidSW": pedid, "formpSW": formp, "conal": cantalm})


def addpedido(request):
    descrip = request.GET["descripf"]
    cantid = request.GET["cantidf"]
    ped = pedido.objects.create(descripcion=descrip, cantidad=cantid)
    ped.save()
    return redirect("/indexpedid")


def addpedidoc(request, id):
    alm = almacenb.objects.get(descripcion=id)
    descrip = alm.descripcion
    cantid = request.GET["cant"]
    ped = pedido.objects.create(descripcion=descrip, cantidad=cantid)
    ped.save()
    return redirect("/indexpedid")


def sumpedido(request, id):
    sum = pedido.objects.get(pk=id)
    sum.cantidad = sum.cantidad+1
    sum.save()
    return redirect("/indexpedid")


def delpedido(request, id):
    sum = pedido.objects.get(pk=id)
    sum.cantidad = sum.cantidad-1
    sum.save()
    if sum.cantidad == 0:
        sum.delete()
    return redirect("/indexpedid")
