from django.shortcuts import render, redirect
from gestion.models import venta, pedido
from almacen.models import inversion, almacenb
from cosmetic.views import cantalm, pront


# Create your views here.


def config(request):
    ventac = venta.objects.all()
    pedidoc = pedido.objects.all()
    inversionc = inversion.objects.all()
    almacenbc = almacenb.objects.all()
    return render(request, "conftempl.html", {"ventaSW": ventac, "pedidoSW": pedidoc, "inversionSW": inversionc, "almacenbSW": almacenbc, "conal": cantalm, "clucSW": pront})


def configdel(request):
    venta.objects.all().delete()
    pedido.objects.all().delete()
    inversion.objects.all().delete()
    almacenb.objects.all().delete()
    return redirect(config)
