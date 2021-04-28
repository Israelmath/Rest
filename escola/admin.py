from django.contrib import admin
from escola.models import Aluno, Curso, Matricula


class ListarAlunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'dataNascimento')
    list_display_links = ('id', 'nome')
    search_fields = (['nome'])
    list_per_page = 20

admin.site.register(Aluno, ListarAlunos)


class ListarCursos(admin.ModelAdmin):
    list_display = ('id', 'cdCurso')
    list_display_links = ('id', 'cdCurso')
    search_fields = (['cdCurso'])

admin.site.register(Curso, ListarCursos)


class ListarMatriculas(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso', 'nivel')
    list_display_links = ('id', 'aluno', 'curso',)

admin.site.register(Matricula, ListarMatriculas)
