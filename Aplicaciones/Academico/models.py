# models.py
from django.db import models


from django.db import models


class Profesor(models.Model):
    id = models.AutoField(primary_key=True)  # Esto especifica el campo id como clave primaria
    nombre = models.CharField(max_length=150)
    telefono = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.nombre

    @property
    def cursos_asignados(self):
        return self.cursos.count()

class Curso(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name="cursos")
    creditos = models.PositiveSmallIntegerField()

    fecha_inicio_inscripcion = models.DateField(null=True, blank=True)
    fecha_fin_inscripcion = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.creditos})"

    @property
    def periodo_inscripcion(self):
        if self.fecha_inicio_inscripcion and self.fecha_fin_inscripcion:
            return f"{self.fecha_inicio_inscripcion} - {self.fecha_fin_inscripcion}"
        return "No definido"
