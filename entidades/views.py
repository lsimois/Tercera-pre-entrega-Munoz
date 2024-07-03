from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

def home(request):
    # Crear el contexto con los juegos de mesa seleccionados aleatoriamente
    contexto = {"juegos_random": Juegos_de_Mesa.objects.order_by('?')[:4], 
                "miniaturas_random": Miniaturas.objects.order_by('?')[:4], "libros_random": Libros.objects.order_by('?')[:4]}
    # Renderizar la plantilla con el contexto
    return render(request, "entidades/index.html", contexto)


def juegos_de_mesa(request):
    contexto = {"juegos_de_mesa": Juegos_de_Mesa.objects.all()}
    return render(request, "entidades/juegos_de_mesa.html", contexto)

def miniaturas(request):
    contexto = {"miniaturas": Miniaturas.objects.all()}
    return render(request, "entidades/miniaturas.html", contexto)

def libros(request):
    contexto = {"libros": Libros.objects.all()}
    return render(request, "entidades/libros.html", contexto)

def acerca_de(request):
    return render(request, "entidades/acerca_de.html")


# Formularios
def miniaturaForm(request):
    if request.method == "POST":
        miForm = MiniaturaForms(request.POST)
        if miForm.is_valid():
            miniatura_codigo = miForm.cleaned_data.get("codigo")
            miniatura_nombre = miForm.cleaned_data.get("nombre")
            miniatura_escala = miForm.cleaned_data.get("escala")
            miniatura_material = miForm.cleaned_data.get("material")
            miniatura_precio = miForm.cleaned_data.get("precio") 
            miniatura = Miniaturas(codigo=miniatura_codigo, nombre=miniatura_nombre, escala=miniatura_escala, material=miniatura_material, precio=miniatura_precio)
            miniatura.save()
            contexto = {"miniaturas":Miniaturas.objects.all() }
            return render(request, "entidades/miniaturas.html", contexto)
    else:
       miForm = MiniaturaForms()
    
    return render(request, "entidades/miniaturaForm.html", {"form": miForm})

def juegos_de_mesaForm(request):
    if request.method == "POST":
        miForm = Juegos_de_MesaForms(request.POST)
        if miForm.is_valid():
            juego_codigo = miForm.cleaned_data.get("codigo")
            juego_nombre = miForm.cleaned_data.get("nombre")
            juego_cant_jugadores = miForm.cleaned_data.get("cant_jugadores")
            juego_edad_recomendada = miForm.cleaned_data.get("edad_recomendada")
            juego_precio = miForm.cleaned_data.get("precio") 
            juego = Juegos_de_Mesa(codigo=juego_codigo, nombre=juego_nombre, cant_jugadores=juego_cant_jugadores, edad_recomendada=juego_edad_recomendada, precio=juego_precio)
            juego.save()
            contexto = {"juegos_de_mesa":Juegos_de_Mesa.objects.all() }
            return render(request, "entidades/juegos_de_mesa.html", contexto)
    else:
       miForm = Juegos_de_MesaForms()
    
    return render(request, "entidades/juegos_de_mesaForm.html", {"form": miForm})

def libroForm(request):
    if request.method == "POST":
        miForm = LibroForms(request.POST)
        if miForm.is_valid():
            libro_codigo = miForm.cleaned_data.get("codigo")
            libro_nombre = miForm.cleaned_data.get("nombre")
            libro_autor = miForm.cleaned_data.get("autor")
            libro_genero = miForm.cleaned_data.get("genero")
            libro_cant_pag = miForm.cleaned_data.get("cant_pag")
            libro_precio = miForm.cleaned_data.get("precio") 
            libro = Libros(codigo=libro_codigo, nombre=libro_nombre, autor=libro_autor, genero=libro_genero, cant_pag=libro_cant_pag,precio=libro_precio)
            libro.save()
            contexto = {"libros":Libros.objects.all() }
            return render(request, "entidades/libros.html", contexto)
    else:
       miForm = LibroForms()
    
    return render(request, "entidades/libroForm.html", {"form": miForm})


#Buscar

def buscarJuegos(request):
    return render(request, "entidades/buscar.html")

def encontrarJuego(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        juegos = Juegos_de_Mesa.objects.filter(nombre__icontains=patron)
        contexto = {"juegos_de_mesa": juegos}
    else:
        contexto = {"juegos_de_mesa": Juegos_de_Mesa.objects.all()}
        
    return render(request, "entidades/juegos_de_mesa.html", contexto)

