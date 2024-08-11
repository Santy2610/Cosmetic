from django.shortcuts import render
from cosmetic.views import cantalm
from datetime import date
from gestion.formulario import vistvent

# Create your views here.


def indexventa(request):
    dat = date.today()
    formc = vistvent(initial={'calef': dat})
    return render(request, "indexventa.html", {"conal": cantalm, "dateSW": dat, "formSW": formc})
