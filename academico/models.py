
from django.db import models


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    duracion_horas = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nombre


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    fecha_registro = models.DateField(auto_now_add=True)

    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name="estudiantes"
    )

    def __str__(self):
        return self.nombre

