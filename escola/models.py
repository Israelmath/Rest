from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=60)
    rg = models.CharField(max_length=8)
    cpf = models.CharField(max_length=11)
    dataNascimento = models.DateField()

    def __str__(self):
        return self.nome

class Curso(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    )
    cdCurso = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default='B')

    def __str__(self):
        return self.descricao
