from django.shortcuts import render, redirect
from cosmetic.views import cantalm
from datetime import date, datetime
from gestion.formulario import vistvent
from gestion.models import venta
from almacen.models import almacenb
from django.db.models import Sum

# Create your views here.


def indexventa(request):
    dat = date.today()
    fechar = request.GET["calef"]
    if fechar == "0000-00-00":
        ven = venta.objects.filter(fecha=dat).order_by(
            'descripcion').annotate(Tot=Sum('cantidad'))
        fechat = dat
    else:
        fechat = datetime.strptime(fechar, "%Y-%m-%d").date()
        ven = venta.objects.filter(fecha=fechat).values('descripcion', 'idalma').order_by(
            'idalma').annotate(tot=Sum('cantidad'))
    alma = almacenb.objects.filter(existencia__gt=0).order_by('descripcion')
    formc = vistvent(initial={'calef': fechat})
    mes = fechat.month
    dia = fechat.day
    year = fechat.year
    return render(request, "indexventa.html", {"conal": cantalm, "dateSW": fechat, "formSW": formc, "venSW": ven,
                                               "almaSW": alma, "mesSW": mes, "diaSW": dia, "yearSW": year})


def addventa(request, fechar, id):
    alma = almacenb.objects.get(pk=id)
    alma.existencia = alma.existencia-1
    ven = venta.objects.create(
        fecha=fechar, descripcion=alma.descripcion, cantidad=1, ganancia=alma.presiob, idalma=alma.id)
    alma.save()
    ven.save()
    return redirect("/indexventa?calef="+fechar)
