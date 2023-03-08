from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render,redirect
from Libreria.models import Usuarios
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate,login,logout


#region Usuarios

def ListadoUsuarios(request):
    paginalistado = open('Libreria/Templates/Usuarios/listado.html')
    lectura = Template(paginalistado.read())
    paginalistado.close()
    usuarios = Usuarios.objects.all()
    parametros = Context({'usuarios':usuarios})
    paginafinal = lectura.render(parametros)
    return HttpResponse(paginafinal)



def InsertarUsuarios(request):
    if request.method == "POST":
     if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('direccion') and request.POST.get('edad') and request.POST.get('telefono') and request.POST.get('cedula') and request.POST.get('correo') and request.POST.get('profesion'):

        usuarios = Usuarios()
        usuarios.Nombre = request.POST.get('nombre')
        usuarios.Apellido = request.POST.get('apellido')
        usuarios.Direccion = request.POST.get('direccion')
        usuarios.Edad = request.POST.get('edad')
        usuarios.Telefono = request.POST.get('telefono')
        usuarios.Cedula = request.POST.get('cedula')
        usuarios.Correo = request.POST.get('correo')
        usuarios.Profesion = request.POST.get('profesion')
        usuarios.save()

        return redirect('/Usuarios/listado')
    else:
        return render(request,'Usuarios/insertar.html')
    



def ActualizarUsuarios(request,idusuarios):
    if request.method == "POST":
     if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('direccion') and request.POST.get('edad') and request.POST.get('telefono') and request.POST.get('cedula') and request.POST.get('correo') and request.POST.get('profesion'):

        usuarios = Usuarios.objects.get(id=idusuarios)
        usuarios.Nombre = request.POST.get('nombre')
        usuarios.Apellido = request.POST.get('apellido')
        usuarios.Direccion = request.POST.get('direccion')
        usuarios.Edad = request.POST.get('edad')
        usuarios.Telefono = request.POST.get('telefono')
        usuarios.Cedula = request.POST.get('cedula')
        usuarios.Correo = request.POST.get('correo')
        usuarios.Profesion = request.POST.get('profesion')
        usuarios.save()

        return redirect('/Usuarios/listado')
    else:
        usuarios = Usuarios.objects.filter(id=idusuarios)
        return render(request,'Usuarios/actualizar.html',{'usuarios':usuarios})
    



def BorrarUsuarios(request,idusuarios):
    usuarios = Usuarios.objects.get(id=idusuarios)
    usuarios.delete()
    return redirect('/Usuarios/listado')


#endregion


#region Libros

# def ListadoLibros(request):

#     paginalistado = open('Libreria/Templates/Libros/listado.html')
#     lectura = Template(paginalistado.read())
#     paginalistado.close()
#     libros = Libros.objects.all()
#     parametros = Context({'libros':libros})
#     paginafinal = lectura.render(parametros)
#     return HttpResponse(paginafinal)

# def InsertarLibros(request):
    


# def ActualizarLibros(request):



# def BorrarLibros(request):


#endregion


#region Login

#endregion