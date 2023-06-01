from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('busca/', views.search, name='busca'),
    path('detalhes/<int:id>', views.detalhes, name='detalhes'),
    path('deletar/<int:id>', views.deletar, name='deletar'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('editar/<int:id>', views.editar, name='editar'),
]