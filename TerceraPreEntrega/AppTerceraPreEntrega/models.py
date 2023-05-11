from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre      = models.CharField(max_length=256)
    apellido    = models.CharField(max_length=256)
    email       = models.EmailField(blank=True)
    telefono    = models.CharField(max_length=20, blank=True)
    dni         = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"

class Vendedor(models.Model):
    username        = models.CharField(max_length=15)
    nombre          = models.CharField(max_length=256)
    apellido        = models.CharField(max_length=256)
    email           = models.EmailField(blank=True)
    telefono        = models.CharField(max_length=20, blank=True)
    dni             = models.CharField(max_length=32)
    fcha_nacimiento = models.DateField(null=True)

    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.dni}"

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=20)
    precio = models.IntegerField(max_length=7)
    stock = models.IntegerField(max_length=4)

    def __str__(self):
        return f"{self.nombre}, {self.marca}, {self.precio}, {self.stock}"

class Venta(models.Model):
    username  = models.ForeignKey(Vendedor)
    cliente   = models.ForeignKey(Cliente)
    producto  = models.CharField(max_length=50)
    cantidad  = models.IntegerField(max_length=2)
    preciotot = models.IntegerField(max_length=9)

    def __str__(self):
        return f"{self.username}, {self.cliente}, {self.producto}, {self.cantidad}"