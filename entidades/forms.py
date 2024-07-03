from django import forms

class MiniaturaForms(forms.Form):
    codigo = forms.IntegerField(required=True)
    nombre = forms.CharField(max_length=50, required=True)
    escala = forms.CharField(max_length=50, required=True)
    material = forms.CharField(max_length=50, required=True)
    precio = forms.DecimalField(max_digits=9, decimal_places=2, required=True)
    
class Juegos_de_MesaForms(forms.Form):
    codigo = forms.IntegerField(required=True)
    nombre= forms.CharField(max_length=50, required=True)
    cant_jugadores = forms.CharField(max_length=50, required=True)
    edad_recomendada = forms.CharField(max_length=50, required=True)
    precio = forms.DecimalField(max_digits=9, decimal_places=2, required=True)
    
class LibroForms(forms.Form):
    codigo = forms.IntegerField(required=True)
    nombre = forms.CharField(max_length=50, required=True)
    autor = forms.CharField(max_length=50, required=True)
    genero = forms.CharField(max_length=50, required=True)
    cant_pag = forms.IntegerField(required=True)
    precio = forms.DecimalField(max_digits=9, decimal_places=2, required=True)