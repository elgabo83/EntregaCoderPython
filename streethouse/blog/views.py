# blog/views.py
from django.shortcuts import render, redirect
from .forms import MarcaForm, PrendaForm, BuscarForm, EventoForm
from .models import Marca, Prenda, Evento

def index(request):
    return render(request, 'blog/index.html')

def incluir_marca(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
    else:
        form = MarcaForm()
    return render(request, 'blog/incluir_marca.html', {'form': form})

def incluir_prenda(request):
    if request.method == 'POST':
        form = PrendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
    else:
        form = PrendaForm()

    return render(request, 'blog/incluir_prenda.html', {'form': form})

def incluir_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
    else:
        form = EventoForm()

    return render(request, 'blog/incluir_evento.html', {'form': form})


def mostrar_resultados(request):
    resultados = {'marcas': [], 'prendas': [], 'eventos': []}

    if request.method == 'POST':
        form = BuscarForm(request.POST)
        if form.is_valid():
            tipo_busqueda = form.cleaned_data['tipo_busqueda']
            query = form.cleaned_data['query']

            if tipo_busqueda == 'marcas':
                resultados['marcas'] = Marca.objects.filter(nombre__icontains=query)
            elif tipo_busqueda == 'prendas':
               
                resultados['prendas'] = Prenda.objects.filter(marca__nombre__icontains=query)
            elif tipo_busqueda == 'eventos':
                resultados['eventos'] = Evento.objects.filter(nombre__icontains=query)
    else:
        form = BuscarForm()

    return render(request, 'blog/mostrar_resultados.html', {'form': form, 'resultados': resultados})



def buscar(request):
    resultados = None
    if request.method == 'POST':
        form = BuscarForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']

            
            resultados_marcas = Marca.objects.filter(nombre__icontains=query)
            resultados_prendas = Prenda.objects.filter(nombre__icontains=query)
            resultados_eventos = Evento.objects.filter(texto__icontains=query)

            resultados = {
                'marcas': resultados_marcas,
                'prendas': resultados_prendas,
                'eventos': resultados_eventos,
            }

    else:
        form = BuscarForm()

    return render(request, 'blog/buscar.html', {'form': form, 'mostrar_resultados': resultados})