from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render
from .models import PersonajePrincipal, Compañero, Ubicacion
from .forms import PersonajePrincipalForm, CompañeroForm, UbicacionForm

# Creo las vistas acá

def inicio(request):
    return render(request, "App/inicio.html")

def busqueda(request):
    return render(request, "App/busqueda.html")

def personajePrincipal(request):
    return render(request, "App/personajes.html")

def compañeros(request):
    return render(request, "App/compañeros.html")

def ubicacion(request):
    return render(request, "App/ubicaciones.html")

def crear(request):
    return render(request, "App/crear.html")



def personajePrincipalForm(request):
    
    if request.method=="POST":
        formpersonaje=PersonajePrincipalForm(request.POST)
        if formpersonaje.is_valid():
            infopersonaje=formpersonaje.cleaned_data
            nombre=infopersonaje["nombre"]
            genero=infopersonaje["genero"]
            raza=infopersonaje["raza"]
            altura=infopersonaje["altura"]
            peso=infopersonaje["peso"]
            personaje=PersonajePrincipal(nombre=nombre, genero=genero, raza=raza, altura=altura, peso=peso)
            personaje.save()
            return render(request, "App/crear.html", {"mensajepersonaje": "Personaje creado exitosamente"})
        else:
            return render(request, "App/crear.html", {"mensaje": "Hubo un error en tu solicitud"})
    else:
        formpersonaje=PersonajePrincipalForm()
        return render(request, "App/personajeformulario.html", {"formulario": formpersonaje})

def compañeroForm(request):
    
    if request.method=="POST":
        formcompañero=CompañeroForm(request.POST)
        if formcompañero.is_valid():
            infocompañero=formcompañero.cleaned_data
            nombre=infocompañero["nombre"]
            genero=infocompañero["genero"]
            raza=infocompañero["raza"]
            compañero=Compañero(nombre=nombre, genero=genero, raza=raza)
            compañero.save()
            return render(request, "App/crear.html", {"mensajecompañero": "Compañero creado exitosamente"})
        else:
            return render(request, "App/crear.html", {"mensaje": "Hubo un error en tu solicitud"})
    else:
        formcompañero=CompañeroForm()
        return render(request, "App/compañeroformulario.html", {"formulario": formcompañero})

def ubicacionForm(request):
    
    if request.method=="POST":
        formubicacion=UbicacionForm(request.POST)
        if formubicacion.is_valid():
            infoubicacion=formubicacion.cleaned_data
            region=infoubicacion["region"]
            aldea=infoubicacion["aldea"]
            siglo=infoubicacion["siglo"]
            ubicacion=Ubicacion(region=region, aldea=aldea, siglo=siglo)
            ubicacion.save()
            return render(request, "App/crear.html", {"mensajeubicacion": "Ubicación creada exitosamente"})
        else:
            return render(request, "App/crear.html", {"mensaje": "Hubo un error en tu solicitud"})
    else:
        formubicacion=UbicacionForm()
        return render(request, "App/ubicacionformulario.html", {"formulario": formubicacion})


def personajeBusqueda(request):
    return render(request, "App/personajebuscar.html")

def personajeBuscar(request):
    if request.GET["nombre"]:
        nombrebuscado=request.GET.get("nombre")
        nombres=PersonajePrincipal.objects.filter(nombre=nombrebuscado)
        if len(nombres)!=0:
            return render(request,"App/resultadobusquedapersonaje.html", {"nombres": nombres})
        else:
            return render(request, "App/personajebuscar.html", {"mensaje": "No existen nombres"})
    else:
        return render(request, "App/personajebuscar.html", {"mensaje": "No ingresaste ninguna busqueda!"})

def compañeroBusqueda(request):
    return render(request, "App/compañerobuscar.html")

def compañeroBuscar(request):
    if request.GET["nombre"]:
        nombrebuscado=request.GET.get("nombre")
        nombres=Compañero.objects.filter(nombre=nombrebuscado)
        if len(nombres)!=0:
            return render(request,"App/resultadobusquedacompañero.html", {"nombres": nombres})
        else:
            return render(request, "App/compañerobuscar.html", {"mensaje": "No existen compañeros"})
    else:
        return render(request, "App/compañerobuscar.html", {"mensaje": "No ingresaste ninguna busqueda!"})

def ubicacionBusqueda(request):
    return render(request, "App/ubicacionbuscar.html")

def ubicacionBuscar(request):
    if request.GET["region"]:
        regionbuscada=request.GET.get("region")
        regiones=Ubicacion.objects.filter(region=regionbuscada)
        if len(regiones)!=0:
            return render(request,"App/resultadobusquedaubicacion.html", {"regiones": regiones})
        else:
            return render(request, "App/ubicacionbuscar.html", {"mensaje": "No existen regiones"})
    else:
        return render(request, "App/ubicacionbuscar.html", {"mensaje": "No ingresaste ninguna busqueda!"})