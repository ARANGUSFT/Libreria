from django.db import models


      
class Libros(models.Model):
     NombreLibro = models.CharField(max_length=150)
     Categoria = models.CharField(max_length=150)
     Paginas = models.CharField(max_length=255)
     Ilustrador = models.CharField(max_length=150)
     Autor = models.CharField(max_length=150)

     class Meta:
      db_table = 'libros'

      

class Usuarios(models.Model):
    Nombre = models.CharField(max_length=255)
    Apellido = models.CharField(max_length=255)
    Direccion = models.CharField(max_length=65)
    Edad = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=20)
    Cedula = models.CharField(max_length=10)
    Correo = models.CharField(max_length=150)
    Profesion = models.CharField(max_length=150)
    libros = models.ForeignKey(Libros,on_delete=models.PROTECT)
    
    class Meta:
      db_table = 'usuarios'

