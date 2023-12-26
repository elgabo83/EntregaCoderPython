from django import forms
from .models import Marca, Prenda, Evento

TIPOS_BUSQUEDA = [
    ('marcas', 'Marcas'),
    ('prendas', 'Prendas'),
    ('eventos', 'eventos'),
]

TIPOS_EVENTO = [
    ('lanzamiento', 'Nuevo Lanzamiento'),
    ('fiesta', 'Fiesta'),
    ('apertura_tienda', 'Apertura de Tienda'),
    ('descuentos', 'Descuentos Especiales'),
    
]

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre']

class EventoForm(forms.ModelForm):
    tipo = forms.ChoiceField(choices=TIPOS_EVENTO)
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Evento
        fields = ['nombre', 'tipo', 'fecha', 'descripcion']

class PrendaForm(forms.ModelForm):
    marca = forms.ModelChoiceField(queryset=Marca.objects.all(), empty_label=None)

    class Meta:
        model = Prenda
        fields = ['nombre', 'marca']

class BuscarForm(forms.Form):
    tipo_busqueda = forms.ChoiceField(choices=TIPOS_BUSQUEDA)
    query = forms.CharField(max_length=100)
