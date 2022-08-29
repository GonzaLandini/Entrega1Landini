from django.urls import path
from .views import *

urlpatterns = [
    path("", inicio, name="inicio"),

    path("personajes/", personajePrincipal, name="personajes"),
    path("personajebuscar/", personajeBusqueda, name="personajebuscar"),
    path("personajeformulario/", personajePrincipalForm, name="personajeformulario"),
    path("resultadobusquedapersonaje/", personajeBuscar, name="resultadobusquedapersonaje" ),
    
    path("compañeros/", compañeros, name="compañeros"),
    path("compañerobuscar/", compañeroBusqueda, name="compañerobuscar"),
    path("compañeroformulario/", compañeroForm, name="compañeroformulario"),
    path("resultadobusquedacompañero/", compañeroBuscar, name="resultadobusquedacompañero"),

    path("ubicaciones/", ubicacion, name="ubicaciones"),
    path("ubicacionbuscar/", ubicacionBusqueda, name="ubicacionbuscar"),
    path("ubicacionformulario/", ubicacionForm, name="ubicacionformulario"),    
    path("resultadobusquedaubicacion/", ubicacionBuscar, name="resultadobusquedaubicacion"),
        
    path("crear/", crear, name="crear"),
    path("busqueda/", busqueda, name="busqueda"),
]