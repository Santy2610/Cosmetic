from django.contrib import admin
from almacen.models import almacenb, inversion
# Register your models here.


class almacenbAdmin(admin.ModelAdmin):
    list_display = ("descripcion", "presioc",
                    "presiob", "ganancia", "cantidad", "existencia")


class inverAdmin(admin.ModelAdmin):
    list_display = ("fecha", "mes", "montoinver", "montoganancia")


admin.site.register(almacenb, almacenbAdmin)
admin.site.register(inversion, inverAdmin)
