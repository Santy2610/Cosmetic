from django.shortcuts import render
from cosmetic.views import cantalm
from datetime import date

# Create your views here.


def indexventa(request):
    dat = date.today()
    return render(request, "indexventa.html", {"conal": cantalm, "dateSW": dat})
