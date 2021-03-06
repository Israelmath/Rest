from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewSet, CursosViewSet, MatriculasViewSet, ListaMatriculasAluno, ListaAlunosMatriculados
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('matriculas', MatriculasViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('explorer/', include(router.urls)),
    path('explorer/aluno/<int:pk>/matriculas', ListaMatriculasAluno.as_view()),
    path('explorer/curso/<int:pk>/alunos', ListaAlunosMatriculados.as_view()),
]
