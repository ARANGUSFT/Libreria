from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render,redirect
from django.db import connection
from Libreria.models import Usuarios,Libros
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


#region Usuarios

def ListadoUsuarios(request):
    listado = connection.cursor()
    listado.execute("call ListadoUsuarios")
    return render(request, 'Usuarios/listado.html', {'usuarios': listado})





def InsertarUsuarios(request):
    #Es necesario tener una cuenta
    if not request.user.is_authenticated:
        return redirect('/Login/login')
    
    if request.method == "POST":
     if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('direccion') and request.POST.get('edad') and request.POST.get('telefono') and request.POST.get('cedula') and request.POST.get('correo') and request.POST.get('profesion') and request.POST.get('libro_id'):

        insertar = connection.cursor()
        insertar.execute("call InsertarUsuarios('"+request.POST.get ('nombre')+"','"+request.POST.get ('apellido')+"','"+request.POST.get ('direccion')+"','"+request.POST.get ('edad')+"','"+request.POST.get ('telefono')+"','"+request.POST.get ('cedula')+"','"+request.POST.get ('correo')+"','"+request.POST.get ('profesion')+"','"+request.POST.get ('libro_id')+"')")

        return redirect('/Usuarios/listado')
    else:
        libros = Libros.objects.all()
        return render(request,'Usuarios/insertar.html',{'libros':libros})
    

 

def ActualizarUsuarios(request,idusuarios):
    #Es necesario tener una cuenta
    if not request.user.is_authenticated:
        return redirect('/Login/login')
       
    if request.method == "POST":
       if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('direccion') and request.POST.get('edad') and request.POST.get('telefono') and request.POST.get('cedula') and request.POST.get('correo') and request.POST.get('profesion') and request.POST.get('libro_id'):
            
            usuarios = Usuarios.objects.get(id=idusuarios)
            actualizar = connection.cursor()
            actualizar.execute("call ActualizarUsuarios('"+ idusuarios +"','"+ request.POST.get('nombre') +"','"+ request.POST.get('apellido') 
            +"','"+ request.POST.get('direccion') +"','"+ request.POST.get('edad') +"','"+ request.POST.get('telefono') +"','"+ request.POST.get('cedula') +"','"+ request.POST.get('correo') +"','"+ request.POST.get('profesion') +"','"+ request.POST.get('libro_id') +"')")
            return redirect('/Usuarios/listado')
    else:
        libros = Libros.objects.all()
        usuarios = Usuarios.objects.filter(id=idusuarios)
        return render(request, 'Usuarios/actualizar.html', {'usuarios':usuarios, 'libros':libros})

    



def BorrarUsuarios(request,idusuarios):
    #Es necesario tener una cuenta
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
    #Es necesario tener una cuenta
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
    #Es necesario tener una cuenta
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
    #Es necesario tener una cuenta
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





#region EditarPerfil

#endregion
