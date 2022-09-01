from django import forms
from .models import Articulo, Proveedor

class DateInput(forms.DateInput):
	input_type = 'date'
	input_formats=['%Y-%m-%d']

class FormularioProductos(forms.Form):
    nombre = forms.CharField()
    precio = forms.FloatField()
    descripcion = forms.CharField(required=False)

class FormularioArticuloDescuento(forms.ModelForm):
    #descuento = forms.FloatField(required=False)
    fecha = forms.DateField(widget=DateInput, label="Fecha")
    class Meta:
        model = Articulo
        fields =  ['nombre', 'precio', 'descripcion', 'fecha', 'categoria', 'imagen', 'proveedores']

    def __init__(self, *args, **kwargs):
        super(FormularioArticuloDescuento, self).__init__(*args, **kwargs)

        self.fields['nombre'].widget.attrs['class'] = "form-control"
        self.fields['precio'].widget.attrs['class'] = "form-control"
        self.fields['descripcion'].widget.attrs['class'] = "form-control"
        self.fields['descripcion'].widget.attrs['style'] = "height:50px;"
        self.fields['categoria'].widget.attrs['class'] = "form-control"
        self.fields['imagen'].widget.attrs['class'] = "form-control"
        self.fields['fecha'].widget.attrs['class'] = "form-control"
        self.fields['proveedores'].widget.attrs['class'] = "form-control"
        #self.fields['descuento'].widget.attrs['class'] = "form-control"


class FormularioProveedor(forms.ModelForm):
    #descuento = forms.FloatField(required=False)
    class Meta:
        model = Proveedor
        fields =  ['nombre']

    def __init__(self, *args, **kwargs):
        super(FormularioProveedor, self).__init__(*args, **kwargs)

        self.fields['nombre'].widget.attrs['class'] = "form-control"
      