import django
from django.db import models
# Create your models here.
python -m django version
class Proveedor(models.Model):
    ruc = models.CharField(max_length=11)
    razon_social = models.CharField(max_length=20)
    telefono = models.CharField(max_length=9)
    def __str__(self):
       return self.razon_social

class Categoria(models.Model):
    codigo = models.CharField(max_length=4)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.codigo}: {self.nombre}'
class Localizacion(models.Model):
  distrito = models.CharField(max_length=20)
  provincia = models.CharField(max_length=20)
  departamento = models.CharField(max_length=20)

  def __str__(self):
      return f'{self.distrito},{self.provincia},{self.departamento}'

class Producto(models.Model):
    # Relaciones
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True)
    proveedor = models.ForeignKey('Proveedor', on_delete=models.SET_NULL, null=True)

    # Atributos
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField()
    precio = models.FloatField()
    estado = models.CharField(max_length=3)
    descuento = models.FloatField(default=0)

  class Colaborador(models.Model):
      reputacion = models.FloatField()
      coberturaEntrega = models.TextField()

class DetallePedido(models.Model):
    #Relaciones
     pedido = models.ForeignKey('Pedido', on_delete=models.SET_NULL, null=True)
    #Atributos
     cantidad = models.IntegerField()
     subtotal = models.FloatField()
     def __str__(self):
         return f'{cantidad}, {subtotal}'







