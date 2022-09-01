from django.urls import path
from . import  views  #CrearArticulo, ListarProveedores, home_view, listar_stock, detalle_articulo, eliminar_articulo,  ActualizarArticulo, EliminarArticulo, DetalleArticulo

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('stock/listar/', views.listar_stock, name='listar_stock'),
    #path('stock/detalle/<int:pk>', views.detalle_articulo, name='detalle'),
    path('stock/eliminar/<int:pk>/', views.eliminar_articulo, name='eliminar_articulo'),
    #path('stock/crear/', crear_articulo, name='crear_articulo'),

    path('stock/crear-articulo/', views.CrearArticulo.as_view(), name='crear_articulo'),

    path('stock/actualizar-articulo/<int:pk>', views.ActualizarArticulo.as_view(), name='actualizar_articulo'),
    path('stock/eliminar-articulo/<int:pk>', views.EliminarArticulo.as_view(), name='eliminar_articulo'),
    path('stock/detalle-articulo/<int:pk>', views.DetalleArticulo.as_view(), name='detalle_articulo'),

    #url de proveedores
    path('proveedores/listar/', views.ListarProveedores.as_view(), name='listar_proveedores'),
    path('proveedores/crear/', views.CrearProveedor.as_view(), name='crear_proveedores'),
    path('proveedores/actualizar/<int:pk>', views.ActualizarProveedores.as_view(), name='actualizar_proveedores'),
    path('proveedores/eliminar/<int:pk>/', views.EliminarProveedores.as_view(), name='eliminar_proveedores'),
]
