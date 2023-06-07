from django.contrib import admin
from .models import Alunos

class AdminAlunos(admin.ModelAdmin):
    list_display = ['id', 'nome', 'matricula', 'ativo']
    search_fields = ['nome']
    list_filter = ['ativo']
    list_display_links = ['nome']
admin.site.register(Alunos, AdminAlunos)