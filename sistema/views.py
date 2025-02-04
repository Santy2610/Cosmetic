from django.shortcuts import render, redirect
from gestion.models import venta, pedido, promot
from almacen.models import inversion, almacenb
from cosmetic.views import cantalm, pront
from sistema.formulario import promtf


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


def codifica(request):
    promo = promot.objects.all()
    formp = promtf()
    return render(request, "codifica.html", {"promoSW": promo, "formpSW": formp, "conal": cantalm})


def addcodifi(request):
    nombr = request.GET["NombF"]
    sal = promot.objects.create(nombre=nombr)
    sal.save()
    return redirect("/codifica")


def delcodifi(request, id):
    sal = promot.objects.get(pk=id)
    sal.delete()
    return redirect("/codifica")
