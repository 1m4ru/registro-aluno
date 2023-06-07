from django.db import models
import hashlib
import random


class Aluno(models.Model):
    matricula = models.CharField(max_length=10, unique=True, blank=True)
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=200)
    contato_emergencia = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='alunos/fotos', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.matricula:
            self.matricula = self.gerar_matricula()
            while Aluno.objects.filter(matricula=self.matricula).exists():
                self.matricula = self.gerar_matricula(str(random.random()))
        super().save(*args, **kwargs)

    def gerar_matricula(self):
        informacoes = self.nome + str(self.data_nascimento)
        hash = hashlib.sha1(informacoes.encode())
        matricula = hash.hexdigest()[:10]
        return matricula

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class DisciplinaRelacionada(models.Model):
    disciplina = models.ForeignKey(
        Disciplina, on_delete=models.CASCADE, related_name='disciplinas_relacionadas')
    disciplina_relacionada = models.ForeignKey(
        Disciplina, on_delete=models.CASCADE, related_name='relacionada_por')

    def __str__(self):
        return f"{self.disciplina} -> {self.disciplina_relacionada}"


class Nota(models.Model):
    aluno = models.ForeignKey('Aluno', on_delete=models.CASCADE)
    disciplina = models.ForeignKey('Disciplina', on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.aluno.nome} - {self.disciplina.nome}: {self.valor}"


class Documento(models.Model):
    aluno = models.ForeignKey('Aluno', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    arquivo = models.FileField(upload_to='documentos/')


class Frequencia(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    data = models.DateField()
    presente = models.BooleanField(default=True)


class RegistroAlteracao(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    campo_alterado = models.CharField(max_length=100)
    valor_anterior = models.CharField(max_length=100)
    data_alteracao = models.DateTimeField(auto_now_add=True)
