from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render,redirect
from Libreria.models import Usuarios,Libros
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


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
    if not request.user.is_authenticated:
        return redirect('/Login/login')
    
    if request.method == "POST":
     if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('direccion') and request.POST.get('edad') and request.POST.get('telefono') and request.POST.get('cedula') and request.POST.get('correo') and request.POST.get('profesion') and request.POST.get('libro_id'):

        usuarios = Usuarios()
        usuarios.Nombre = request.POST.get('nombre')
        usuarios.Apellido = request.POST.get('apellido')
        usuarios.Direccion = request.POST.get('direccion')
        usuarios.Edad = request.POST.get('edad')
        usuarios.Telefono = request.POST.get('telefono')
        usuarios.Cedula = request.POST.get('cedula')
        usuarios.Correo = request.POST.get('correo')
        usuarios.Profesion = request.POST.get('profesion')
        usuarios.libros = request.POST.get('libro_id')
        usuarios.save()

        return redirect('/Usuarios/listado')
    else:
        return render(request,'Usuarios/insertar.html')
    



def ActualizarUsuarios(request,idusuarios):
    if not request.user.is_authenticated:
        return redirect('/Login/login')
       
    if request.method == "POST":
     if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('direccion') and request.POST.get('edad') and request.POST.get('telefono') and request.POST.get('cedula') and request.POST.get('correo') and request.POST.get('profesion') and request.POST.get('libro_id'):

        usuarios = Usuarios.objects.get(id=idusuarios)
        usuarios.Nombre = request.POST.get('nombre')
        usuarios.Apellido = request.POST.get('apellido')
        usuarios.Direccion = request.POST.get('direccion')
        usuarios.Edad = request.POST.get('edad')
        usuarios.Telefono = request.POST.get('telefono')
        usuarios.Cedula = request.POST.get('cedula')
        usuarios.Correo = request.POST.get('correo')
        usuarios.Profesion = request.POST.get('profesion')
        usuarios.libros = request.POST.get('libro_id')
        usuarios.save()

        return redirect('/Usuarios/listado')
    else:
        usuarios = Usuarios.objects.filter(id=idusuarios)
        return render(request,'Usuarios/actualizar.html',{'usuarios':usuarios})
    



def BorrarUsuarios(request,idusuarios):
    if not request.user.is_authenticated:
        return redirect('/Login/login')
    
    usuarios = Usuarios.objects.get(id=idusuarios)
    usuarios.delete()
    return redirect('/Usuarios/listado')


#endregion




#region Libros

def ListadoLibros(request):
    paginalistado = open('Libreria/Templates/Libros/listado.html')
    lectura = Template(paginalistado.read())
    paginalistado.close()
    libros = Libros.objects.all()
    parametros = Context({'libros':libros})
    paginafinal = lectura.render(parametros)
    return HttpResponse(paginafinal)



def InsertarLibros(request):
    if not request.user.is_authenticated:
        return redirect('/Login/login')
    
    if request.method == "POST":
     if request.POST.get('nombrelibro') and request.POST.get('categoria') and request.POST.get('paginas') and request.POST.get('ilustrador') and request.POST.get('autor'):

        libros = Libros()
        libros.NombreLibro = request.POST.get('nombrelibro')
        libros.Categoria = request.POST.get('categoria')
        libros.Paginas = request.POST.get('paginas')
        libros.Ilustrador = request.POST.get('ilustrador')
        libros.Autor = request.POST.get('autor')
        libros.save()

        return redirect('/Libros/listado')
    else:
        return render(request,'Libros/insertar.html')
    



def ActualizarLibros(request,idlibros):
    if not request.user.is_authenticated:
        return redirect('/Login/login')
    
    if request.method == "POST":
     if request.POST.get('nombrelibro') and request.POST.get('categoria') and request.POST.get('paginas') and request.POST.get('ilustrador') and request.POST.get('autor'):

        libros = Libros.objects.get(id=idlibros)
        libros.NombreLibro = request.POST.get('nombrelibro')
        libros.Categoria = request.POST.get('categoria')
        libros.Paginas = request.POST.get('paginas')
        libros.Ilustrador = request.POST.get('ilustrador')
        libros.Autor = request.POST.get('autor')
        libros.save()

        return redirect('/Libros/listado')
    else:
        libros = Libros.objects.filter(id=idlibros)
        return render(request,'Libros/actualizar.html',{'libros':libros})



def BorrarLibros(request,idlibros):
    if not request.user.is_authenticated:
        return redirect('/Login/login')
    
    libros = Libros.objects.get(id=idlibros)
    libros.delete()
    return redirect('/Libros/listado')

#endregion




#region Login

def Registro(request):
    if request.method == "POST":
     if request.POST.get('username') and request.POST.get('email') and request.POST.get('password'):

        registro = User.objects.create_user(username=request.POST.get('username'),email=request.POST.get('email'),password=request.POST.get('password'))
        registro.save()

        return redirect('/Login/login')
    else:
        return render(request,'Login/registro.html')


def Login(request):
    if request.method == "POST":
        if request.POST.get('username') and request.POST.get('password'):
           user = authenticate(username=request.POST.get('username'),password=request.POST.get('password'))

        if user is not None:
             login(request,user)
             return redirect('/Libros/listado')
        else:
            mensaje = "Usuario o contraseña estan mal"
            return render(request,'Login/login.html',{'mensaje':mensaje})
    
    else:
        return render(request,'Login/login.html')




def Logout(request):
    logout(request)
    return redirect('/Login/login')

#endregion