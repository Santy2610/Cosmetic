from django.shortcuts import render


def principal(request):
    return render(request, "index.html")
