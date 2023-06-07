from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Alunos(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    matricula = models.CharField(max_length=255)
    imagem = models.ImageField()
    telefone = models.CharField(max_length=20)
    endereco = models.TextField()
    info = models.TextField()
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Alunos'