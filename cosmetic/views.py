from django.shortcuts import render
from almacen.models import almacenb
from django.db.models import Sum


def cantalm():
    res = 0
    cont = almacenb.objects.order_by(
        'descripcion').annotate(conta=Sum('existencia'))
    for cont in cont:
        res = res+cont.conta
    return res


def principal(request):
    return render(request, "index.html", {"conal": cantalm})
