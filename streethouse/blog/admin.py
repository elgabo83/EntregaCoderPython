# blog/admin.py

from django.contrib import admin
from .models import Marca, Prenda, Evento

admin.site.register(Marca)
admin.site.register(Prenda)
admin.site.register(Evento)
