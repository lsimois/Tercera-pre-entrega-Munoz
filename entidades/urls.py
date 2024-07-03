from django.urls import path, include
from entidades.views import *


urlpatterns = [
    path('', home, name="home"),
    path('juegos_de_mesa/', juegos_de_mesa, name="juegos_de_mesa"),
    path('miniaturas/', miniaturas, name="miniaturas"),
    path('libros/', libros, name="libros"),
    path('acerca_de/', acerca_de, name="acerca_de"),
    
    #Formularios
    path('miniaturaForm/', miniaturaForm, name="miniaturaForm"),
    path('juegos_de_mesaForm/', juegos_de_mesaForm, name="juegos_de_mesaForm"),
    path('libroFrom/', libroForm, name="libroFrom"),

    #Buscar
    path('buscarJuegos/', buscarJuegos, name="buscarJuegos"),
    path('encontrarJuego/', encontrarJuego, name="encontrarJuego"),

]

