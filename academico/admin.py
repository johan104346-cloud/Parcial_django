
from django.contrib import admin
from .models import Curso, Estudiante


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "duracion_horas")
    search_fields = ("nombre",)


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "correo", "curso", "fecha_registro")
    search_fields = ("nombre", "correo")
    list_filter = ("curso", "fecha_registro")
