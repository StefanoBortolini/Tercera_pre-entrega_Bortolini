from django import forms


class ClienteFormulario(forms.Form):
    nombre      = forms.CharField(required=True, max_length=40) 
    apellido    = forms.CharField(required=True, max_length=40)
    email       = forms.EmailField(required=False)
    telefono    = forms.CharField(required=False, max_length=20)
    dni         = forms.CharField(required=True, max_length=32)

class VendedorFormulario(forms.Form):
    username        = forms.CharField(required=True, max_length=15)
    nombre          = forms.CharField(required=True, max_length=256)
    apellido        = forms.CharField(required=True, max_length=256)
    email           = forms.EmailField(required=True)
    telefono        = forms.CharField(required=True, max_length=20)
    dni             = forms.CharField(required=True, max_length=32)
    fcha_nacimiento = forms.DateField(required=True)

class ProductoFormulario(forms.Form):
    nombre  = forms.CharField(required=True, max_length=30)
    marca   = forms.CharField(required=True, max_length=20)
    precio  = forms.IntegerField()
    stock   = forms.IntegerField()