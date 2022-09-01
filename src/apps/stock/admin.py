from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.Articulo)

admin.site.register(models.Categoria)
admin.site.register(models.Proveedor)
#admin.site.register(ProveedorDistribuye)