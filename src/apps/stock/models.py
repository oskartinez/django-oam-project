from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=30)
    domicilio = models.CharField(max_length=90, null=True, blank=True)
    telefono = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Proveedores'
    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.FloatField()
    fecha = models.DateTimeField(default=None, null=True)
    descripcion = models.CharField(max_length=50, default='-')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=True, null=True)
    imagen = models.ImageField(upload_to='imagenes_productos/', null=True, blank=True)
    proveedores = models.ManyToManyField(Proveedor)

    def __str__(self):
        return self.nombre



# class ProveedorDistribuye(models.Model):
#     articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
#     proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

#     class Meta:
#         verbose_name_plural = 'Proveedores Distribuyen'
#     def __str__(self):
#         return f'Clase ProveedorDistribuye - Objeto ID {self.id}'


