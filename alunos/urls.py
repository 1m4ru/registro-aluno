from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alunos/<int:aluno_id>/', views.info, name='info'),
    path('alunos/<int:aluno_id>/detalhes_aluno/',
         views.detalhes_aluno, name='detalhes_aluno'),
    path('alunos/<int:aluno_id>/editar_aluno/',
         views.editar_aluno, name='editar_aluno'),
    path('alunos/<int:aluno_id>/deletar/', views.deletar, name='deletar'),
    path('alunos/adicionar_aluno/', views.adicionar_aluno, name='adicionar_aluno'),
    path('ver-notas/', views.ver_notas, name='ver_notas'),
    path('alunos/<int:aluno_id>/ver-media/',
         views.ver_media, name='ver_media'),
    path('frequencia/', views.consultar_frequencia, name='consultar_frequencia'),
    path('relatorios/media-turma/', views.media_turma, name='media_turma'),
    path('relatorios/indice-presenca/',
         views.indice_presenca, name='indice_presenca'),
]
