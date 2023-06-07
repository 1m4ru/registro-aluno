from django import forms
from .models import Aluno, Nota

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'data_nascimento', 'endereco', 'contato_emergencia']

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['disciplina', 'valor']
