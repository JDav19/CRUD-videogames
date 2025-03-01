"""
URL configuration for juegos_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from juegos_app.views import JuegoListado, JuegoDetalle, JuegoCrear, JuegoActualizar, JuegoEliminar
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # La ruta 'leer' en donde listamos todos los registros o juegos de la Base de Datos
    path('juegos/', JuegoListado.as_view(template_name="juegos/index.html"), name='leer'),

    # La ruta 'detalles' en donde mostraremos una página con los detalles de un juego o registro
    path('juegos/detalle/<int:pk>', JuegoDetalle.as_view(template_name="juegos/detalles.html"), name='detalles'),

    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo juego o registro
    path('juegos/crear', JuegoCrear.as_view(template_name="juegos/crear.html"), name='crear'),

    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un juego o registro de la Base de Datos
    path('juegos/editar/<int:pk>', JuegoActualizar.as_view(template_name="juegos/actualizar.html"), name='actualizar'),

    # La ruta 'eliminar' que usaremos para eliminar un juego o registro de la Base de Datos
    path('juegos/eliminar/<int:pk>', JuegoEliminar.as_view(), name='eliminar'),
]

# Solo en desarrollo: Sirve archivos multimedia
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
