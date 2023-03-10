"""Libreria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#Usuarios
from Libreria.views import ListadoUsuarios,InsertarUsuarios,ActualizarUsuarios,BorrarUsuarios
# Libros
from Libreria.views import ListadoLibros,InsertarLibros,ActualizarLibros,BorrarLibros
#Login
from Libreria.views import Registro,Login,Logout


urlpatterns = [
    path('admin/', admin.site.urls),
    
    #Usuarios
    path("Usuarios/listado", ListadoUsuarios),
    path("Usuarios/insertar", InsertarUsuarios),
    path("Usuarios/actualizar/<str:idusuarios>", ActualizarUsuarios),
    path("Usuarios/borrar/<int:idusuarios>", BorrarUsuarios),
    #Libros
    path("Libros/listado", ListadoLibros),
    path("Libros/insertar", InsertarLibros),
    path("Libros/actualizar/<int:idlibros>", ActualizarLibros),
    path("Libros/borrar/<int:idlibros>", BorrarLibros),
    #Login
    path("Login/login", Login),
    path("Login/registro", Registro),
    path("Login/logout", Logout),
   
]
