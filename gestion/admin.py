from django.contrib import admin
from gestion.models import venta, pedido

# Register your models here.


class ventaAdmin(admin.ModelAdmin):
    list_display = ("fecha", "descripcion", "cantidad",
                    "ganancia", "presioc", "idalma")


class pedidoAdmin(admin.ModelAdmin):
    list_display = ("descripcion", "cantidad")


admin.site.register(venta, ventaAdmin)
admin.site.register(pedido, pedidoAdmin)
