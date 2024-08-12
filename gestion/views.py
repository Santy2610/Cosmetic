from django.shortcuts import render
from cosmetic.views import cantalm
from datetime import date
from gestion.formulario import vistvent
from gestion.models import venta
from almacen.models import almacenb

# Create your views here.


def indexventa(request):
    dat = date.today()
    fechar = request.GET["calef"]
    if fechar == "0000-00-00":
        ven = venta.objects.filter(fecha=dat).order_by('fecha')
        fechar = dat
    else:
        ven = venta.objects.filter(fecha=fechar).order_by('fecha')

    alma = almacenb.objects.filter(existencia__gt=0).order_by('descripcion')

    formc = vistvent(initial={'calef': fechar})
    return render(request, "indexventa.html", {"conal": cantalm, "dateSW": fechar, "formSW": formc, "venSW": ven, "almaSW": alma})
