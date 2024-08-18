from django.shortcuts import render
from almacen.models import almacenb
from django.db.models import Sum
from gestion.formulario import vistvent


def cantalm():
    res = 0
    cont = almacenb.objects.order_by(
        'descripcion').annotate(conta=Sum('existencia'))
    for cont in cont:
        res = res+cont.conta
    return res


def principal(request):
    ventaM = []
    noventaM = []
    control = 0
    ventaR = almacenb.objects.order_by('descripcion', 'existencia').annotate(
        cant=Sum('cantidad'), exst=Sum('existencia'))
    for ventaR in ventaR:

        resvent = ventaR.cant-ventaR.exst
        if resvent > 0:
            porc = (resvent/ventaR.cant)*100
            porc = int(porc)
            ventaM.append({
                'descricion': ventaR.descripcion,
                'cantidad': ventaR.cant,
                'existencia': ventaR.exst,
                'venta': resvent,
                'porciento': porc
            })
        else:
            porc = (resvent/ventaR.cant)*100
            porc = int(porc)
            noventaM.append({
                'descricion': ventaR.descripcion,
                'cantidad': ventaR.cant,
                'existencia': ventaR.exst,
                'venta': resvent,
                'porciento': porc
            })

    return render(request, "index.html", {"conal": cantalm, "ventaMSW": ventaM, "noventaMSW": noventaM})
