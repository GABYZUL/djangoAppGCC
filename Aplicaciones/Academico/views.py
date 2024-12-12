from django.shortcuts import render, redirect
from .models import Curso
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import Profesor
from django.contrib import messages

def listarProfesores(request):
    profesores = Profesor.objects.all()  # Obtiene todos los profesores
    return render(request, "listar_profesores.html", {"profesores": profesores})

def agregarProfesor(request):
    if request.method == 'POST':
        nombre = request.POST['txtNombre']
        telefono = request.POST['txtTelefono']
        
        # Crear un nuevo profesor
        profesor = Profesor.objects.create(
            nombre=nombre,
            telefono=telefono
        )

        messages.success(request, f"Profesor {profesor.nombre} agregado correctamente.")
        return redirect('listar_profesores')  # Redirige a la lista de profesores

    return render(request, "agregar_profesor.html")


def home(request):
    cursosListados = Curso.objects.all()
    return render(request, "gestionCursos.html", {"cursos": cursosListados})

def principal(request):
    # Obtener todos los profesores
    profesores = Profesor.objects.all()
    cursosListados = Curso.objects.all()

    return render(request, "principal.html", {"cursos": cursosListados, "profesores": profesores})


def registrarCurso(request):
    if request.method == 'POST':
        codigo = request.POST['txtCodigo']
        nombre = request.POST['txtNombre']
        profesor_id = request.POST['txtProfesor']  # Obtener el id del profesor seleccionado
        creditos = request.POST['numCreditos']
        fecha_inicio_inscripcion = request.POST['fechaInicioInscripcion']
        fecha_fin_inscripcion = request.POST['fechaFinInscripcion']

        # Obtener el profesor por su ID
        profesor = Profesor.objects.get(id=profesor_id)

        # Crear un nuevo curso con el profesor asignado
        curso = Curso.objects.create(
            codigo=codigo,
            nombre=nombre,
            profesor=profesor,  # Asociar el profesor al curso
            creditos=creditos,
            fecha_inicio_inscripcion=fecha_inicio_inscripcion,
            fecha_fin_inscripcion=fecha_fin_inscripcion
        )
        
        return redirect('/principal.html')  # O la URL que corresponda


def edicionCurso(request, codigo):
    curso = get_object_or_404(Curso, codigo=codigo)

    # Formatear las fechas en el formato correcto para el campo de fecha en HTML
    fecha_inicio_inscripcion = curso.fecha_inicio_inscripcion.strftime('%Y-%m-%d') if curso.fecha_inicio_inscripcion else ''
    fecha_fin_inscripcion = curso.fecha_fin_inscripcion.strftime('%Y-%m-%d') if curso.fecha_fin_inscripcion else ''

    return render(request, "edicionCurso.html", {
        "curso": curso,
        "fecha_inicio_inscripcion": fecha_inicio_inscripcion,
        "fecha_fin_inscripcion": fecha_fin_inscripcion
    })


def editarCurso(request):
    if request.method == 'POST':
        # Captura de datos del formulario
        codigo = request.POST['txtCodigo']
        nombre = request.POST['txtNombre']
        creditos = request.POST['numCreditos']
        profesor = request.POST['txtProfesor']  # Capturar el campo profesor
        fecha_inicio_inscripcion = request.POST['fechaInicioInscripcion']  # Capturar la fecha de inicio
        fecha_fin_inscripcion = request.POST['fechaFinInscripcion']  # Capturar la fecha de fin

        # Obtener el curso y actualizar los campos
        curso = Curso.objects.get(codigo=codigo)
        curso.nombre = nombre
        curso.creditos = creditos
        curso.profesor = profesor  # Actualizar el campo profesor
        curso.fecha_inicio_inscripcion = fecha_inicio_inscripcion  # Actualizar la fecha de inicio
        curso.fecha_fin_inscripcion = fecha_fin_inscripcion  # Actualizar la fecha de fin
        curso.save()



        return redirect('/principal.html')


def eliminarCurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()


    return redirect('/')
