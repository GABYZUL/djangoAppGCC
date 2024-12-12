from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarCurso/', views.registrarCurso),
    path('edicionCurso/<codigo>', views.edicionCurso),
    path('editarCurso/', views.editarCurso),
    path('eliminarCurso/<codigo>', views.eliminarCurso),
    path('principal.html', views.principal),
    path('gestionCursos.html', views.home),
    path('listar_profesores.html', views.listarProfesores),
    path('agregar_profesores.html', views.agregarProfesor),
]