from django.contrib import admin
from .forms import RegModelForm
from .models import Seccion_producto, Producto, Registrado


class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio','stock','seccion']
    search_fields = ['nombre']
    list_filter = ['seccion']
    list_per_page = 10



admin.site.register(Seccion_producto)
admin.site.register(Producto,ProductoAdmin)

class AdminRegistrado(admin.ModelAdmin):
    list_display = ["email","nombre","timestamp"]
    form = RegModelForm
    list_filter = ["timestamp"]
    list_editable = ["nombre"]
    search_fiellds = ["email","nombre"]


    #class Meta:
    #    model = Registrado
admin.site.register(Registrado,AdminRegistrado)