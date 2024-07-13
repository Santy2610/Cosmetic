from django.shortcuts import render
from almacen.models import almacenb

# Create your views here.


def indexalm(request):
    return render(request, "indexal.html")


def indexinv(request):
    return render(request, "indexinv.html")
