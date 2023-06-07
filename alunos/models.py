from django.db import models

class Aluno(models.Model):
    matricula = models.CharField(max_length=50, unique=True)
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=200)
    contato_emergencia = models.CharField(max_length=100)    
    foto = models.ImageField(upload_to='alunos/fotos', null=True, blank=True)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class DisciplinaRelacionada(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='disciplinas_relacionadas')
    disciplina_relacionada = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='relacionada_por')

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