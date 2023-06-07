from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('busca/', views.search, name='busca'),
    path('info/<int:id>', views.info, name='info'),
    path('deletar/<int:id>', views.deletar, name='deletar'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('editar/<int:id>', views.editar, name='editar'),
]