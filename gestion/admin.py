from django.contrib import admin
from gestion.models import venta

# Register your models here.


class ventaAdmin(admin.ModelAdmin):
    list_display = ("fecha", "descripcion", "cantidad", "ganancia")


admin.site.register(venta, ventaAdmin)
