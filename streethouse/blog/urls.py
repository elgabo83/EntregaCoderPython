# blog/urls.py
from django.urls import path
from .views import index, incluir_marca, incluir_prenda, mostrar_resultados, buscar, incluir_evento

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('incluir_marca/', incluir_marca, name='incluir_marca'),
    path('incluir_prenda/', incluir_prenda, name='incluir_prenda'),
    path('mostrar_resultados/', mostrar_resultados, name='mostrar_resultados'),
    path('buscar/', buscar, name='buscar'),
    path('incluir_evento/', incluir_evento, name='incluir_evento'),
   
]
