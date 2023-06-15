from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('alunos/<int:aluno_id>/', views.info, name='info'),
    path('alunos/<int:aluno_id>/editar/', views.editar, name='editar'),
    path('alunos/<int:aluno_id>/deletar/', views.deletar, name='deletar'),
    path('alunos/adicionar/', views.adicionar, name='adicionar'),
    path('alunos/<int:aluno_id>/ver-notas/', views.ver_notas, name='ver_notas'),
    path('alunos/<int:aluno_id>/ver-media/', views.ver_media, name='ver_media'),
    path('frequencia/', views.consultar_frequencia, name='consultar_frequencia'),
    path('relatorios/media-turma/', views.media_turma, name='media_turma'),
    path('relatorios/indice-presenca/', views.indice_presenca, name='indice_presenca'),
]
