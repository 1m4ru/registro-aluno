from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno, Nota, Documento, Frequencia, RegistroAlteracao
from .forms import AlunoForm, NotaForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

@login_required
def index(request):
    alunos = Aluno.objects.all()
    return render(request, 'pages/index.html', {'alunos': alunos})

def info(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    context = {'aluno': aluno}
    return render(request, 'pages/info.html', context)

def adicionar(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST, request.FILES)
        if form.is_valid():
            aluno = form.save(commit=False)
            aluno.matricula = gerar_matricula()  # Geração automática da matrícula
            aluno.save()
            return redirect('home')
    else:
        form = AlunoForm()
    
    return render(request, 'pages/base.html', {'form': form})

def gerar_matricula():
    # Recupera o último aluno cadastrado
    ultimo_aluno = Aluno.objects.order_by('-id').first()

    if ultimo_aluno:
        # Se existir um aluno cadastrado, gera uma nova matrícula sequencial
        nova_matricula = ultimo_aluno.matricula + 1
    else:
        # Se não existir nenhum aluno cadastrado, define a matrícula inicial como 1
        nova_matricula = 1

    return nova_matricula

def detalhes_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    return render(request, 'pages/detalhes_aluno.html', {'aluno': aluno})

def editar(request, aluno_id):
    aluno = Aluno.objects.get(id=aluno_id)

    if request.method == 'POST':
        aluno.nome = request.POST.get('nome')
        aluno.data_nascimento = request.POST.get('data_nascimento')
        aluno.endereco = request.POST.get('endereco')
        aluno.contato_emergencia = request.POST.get('contato_emergencia')
        # Adicione outros campos de acordo com suas necessidades

        aluno.save()
        return redirect('detalhes_aluno', aluno_id=aluno.id)

    return render(request, 'pages/editar_aluno.html', {'aluno': aluno})


def deletar(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)

    if request.method == 'POST':
        aluno.delete()
        return redirect('index')  # Redireciona para a página inicial após a exclusão

    return render(request, 'confirmar_exclusao.html', {'aluno': aluno})

def registrar_nota(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NotaForm()
    return render(request, 'registrar_nota.html', {'form': form})

def ver_notas(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    notas = Nota.objects.filter(aluno=aluno)
    return render(request, 'pages/ver_notas.html', {'aluno': aluno, 'notas': notas})


def calcular_media(notas):
    total_notas = len(notas)
    soma_notas = sum(nota.valor for nota in notas)
    if total_notas > 0:
        return soma_notas / total_notas
    return 0

def ver_media(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    notas = Nota.objects.filter(aluno=aluno)
    total_notas = notas.count()
    media = sum(nota.valor for nota in notas) / total_notas if total_notas > 0 else 0
    return render(request, 'ver_media.html', {'aluno': aluno, 'media': media})

def consultar_informacoes(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    notas = Nota.objects.filter(aluno=aluno)
    frequencias = Frequencia.objects.filter(aluno=aluno)
    
    # Outras consultas de informações podem ser adicionadas aqui
    
    return render(request, 'consultar_informacoes.html', {'aluno': aluno, 'notas': notas, 'frequencias': frequencias})

def editar_informacoes(request, aluno_id):
    
    aluno = get_object_or_404(Aluno, id=aluno_id)
    if request.method == 'POST':
        # Processar os dados enviados pelo formulário
        nome = request.POST.get('nome')
        matricula = request.POST.get('matricula')
        # Atualizar as informações pessoais do aluno
        aluno.nome = nome
        aluno.matricula = matricula
        # Salvar as alterações no aluno
        aluno.save()

        # Registrar a alteração no histórico
        registro = RegistroAlteracao(aluno=aluno, campo_alterado='informacoes_pessoais', valor_anterior='Valores anteriores')
        registro.save()

        return redirect('detalhes_aluno', aluno_id=aluno.id)
    else:
        # Exibir o formulário preenchido com as informações atuais
        return render(request, 'editar.html', {'aluno': aluno})


def adicionar_documento(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        arquivo = request.FILES.get('arquivo')

        documento = Documento(aluno=aluno, titulo=titulo, arquivo=arquivo)
        documento.save()

        return redirect('detalhes_aluno', aluno_id=aluno.id)
    else:
        return render(request, 'adicionar_documento.html', {'aluno': aluno})

def consultar_frequencia(request):
    frequencias = Frequencia.objects.all()
    return render(request, 'pages/consultar_frequencia.html', {'frequencias': frequencias})

def media_turma(request):
    # Calcula a média da turma
    media = Aluno.objects.all().aggregate(media_geral=Avg('nota'))
    return render(request, 'relatorios/media_turma.html', {'media': media})

def indice_presenca(request):
    # Calcula o índice de presença da turma
    indice = Aluno.objects.all().aggregate(indice_presenca=Avg('presenca'))
    return render(request, 'relatorios/indice_presenca.html', {'indice': indice})