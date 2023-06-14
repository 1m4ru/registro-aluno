# forms.py
from django.contrib import admin
from .models import Aluno, Disciplina, Nota, Frequencia


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'nome', 'data_nascimento',
                    'endereco', 'contato_emergencia')
    list_filter = ['data_nascimento']
    search_fields = ['nome', 'matricula']


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']


@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'disciplina', 'nota_01', 'nota_02', 'nota_03')


@admin.register(Frequencia)
class FrequenciaAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'disciplina', 'data', 'presente')
    list_filter = ('disciplina',)
