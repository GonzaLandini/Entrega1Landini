from django import forms

class PersonajePrincipalForm(forms.Form):
    #Especificar los campos
    nombre=forms.CharField(max_length=50)
    genero=forms.CharField(max_length=50)
    raza=forms.CharField(max_length=50)
    altura=forms.IntegerField()
    peso=forms.IntegerField()

class CompañeroForm(forms.Form):
    #Especificar los campos
    nombre=forms.CharField(max_length=50)
    genero=forms.CharField(max_length=50)
    raza=forms.CharField(max_length=50)

class UbicacionForm(forms.Form):
    #Especificar los campos
    region=forms.CharField(max_length=50)
    aldea=forms.CharField(max_length=50)
    siglo=forms.IntegerField()