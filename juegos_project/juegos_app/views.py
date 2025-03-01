from django.shortcuts import render

# Create your views here.
from .models import Juego

# Instanciamos las vistas genéricas de Django
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Nos sirve para redireccionar después de una acción revertiendo patrones de expresiones regulares
from django.urls import reverse

# Habilitamos el uso de mensajes en Django
from django.contrib import messages

# Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin

# Habilitamos los formularios en Django
from django import forms
from .forms import JuegoForm  # Importamos el formulario personalizado

class JuegoListado(ListView):
    model = Juego  # Llamamos a la clase 'Juego' que se encuentra en nuestro archivo 'models.py'
    template_name = 'juegos/index.html'  # Asegúrate de que la plantilla exista

class JuegoCrear(SuccessMessageMixin, CreateView):
    model = Juego  # Llamamos a la clase 'Juego' que se encuentra en nuestro archivo 'models.py'
    form_class = JuegoForm  # Usamos el formulario personalizado
    template_name = 'juegos/crear.html'
    success_message = 'Juego Creado Correctamente!'  # Mostramos este Mensaje luego de Crear un Juego

    # Redireccionamos a la página principal luego de crear un registro o juego
    def get_success_url(self):
        return reverse('leer')  # Redireccionamos a la vista principal 'leer'

class JuegoDetalle(DetailView):
    model = Juego  # Llamamos a la clase 'Juego' que se encuentra en nuestro archivo 'models.py'
    template_name = 'juegos/detalles.html'

class JuegoActualizar(SuccessMessageMixin, UpdateView):
    model = Juego  # Llamamos a la clase 'Juego' que se encuentra en nuestro archivo 'models.py'
    form_class = JuegoForm  # Usamos el formulario personalizado
    template_name = 'juegos/actualizar.html'
    success_message = 'Juego Actualizado Correctamente!'  # Mostramos este Mensaje luego de Editar un Juego

    # Redireccionamos a la página principal luego de actualizar un registro o juego
    def get_success_url(self):
        return reverse('leer')  # Redireccionamos a la vista principal 'leer'

class JuegoEliminar(SuccessMessageMixin, DeleteView):
    model = Juego
    template_name = 'juegos/eliminar.html'  # Asegúrate de crear esta plantilla

    # Redireccionamos a la página principal luego de eliminar un registro o juego
    def get_success_url(self):
        success_message = 'Juego Eliminado Correctamente!'  # Mostramos este Mensaje luego de Eliminar un Juego
        messages.success(self.request, success_message)
        return reverse('leer')  # Redireccionamos a la vista principal 'leer'
