"""cosmetic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cosmetic.views import principal
from almacen.views import indexalm, indexinv, invadd, invdell, invupdate, almadd, almadel, listalmacen, cal, invt, invereport
from gestion.views import indexventa, addventa, dismventa, reportvent, indexpedid, addpedido, sumpedido, delpedido, addpedidoc, reportpedido

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', principal),

    path('indexalm/<dato>/<valor>', indexalm),
    path('almadd/<dato>', almadd),
    path('almadel/<dato>/<id>', almadel),
    path('listalmacen', listalmacen),
    path('cal', cal),
    path('invt', invt),

    path('indexinv/<edit>/<dato>', indexinv),
    path('invadd', invadd),
    path('invdell/<dato>', invdell),
    path('invupdate/<dato>', invupdate),
    path('invereport', invereport),

    path('indexventa', indexventa),
    path('addventa/<fechar>/<id>', addventa),
    path('dismventa/<fechar>/<id>', dismventa),
    path('reportvent/<date>', reportvent),
    path('indexpedid', indexpedid),
    path('addpedido', addpedido),
    path('addpedidoc/<id>', addpedidoc),
    path('sumpedido/<id>', sumpedido),
    path('delpedido/<id>', delpedido),
    path('reportpedido', reportpedido),
]
