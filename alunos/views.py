from django.shortcuts import render, redirect, get_object_or_404
from . models import Alunos
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='login')
def index(request):
    alunos = Alunos.objects.filter(usuario_id=request.user.id).order_by('-id')
    return render(request, 'pages/index.html', {'alunos':alunos})

def search(request):
    q = request.GET.get('search')
    alunos = Alunos.objects.filter(nome__icontains=q)
    return render(request, 'pages/index.html', {'alunos':alunos})

def deletar(request, id):
    aluno = Alunos.objects.get(id=id)
    aluno.delete()
    return redirect('home')

def adicionar(request):

    if request.method == 'POST':
        nome = request.POST.get('nome')
        matricula = request.POST.get('matricula')
        outras_info = request.POST.get('outras_info')
        data = request.POST.get('data_nasc')
        telefone = request.POST.get('telefone')
        imagem = request.FILES.get('imagem')
        print(imagem)
        novo_aluno = Alunos(usuario_id=request.user.id,nome=nome,cpf=cpf, email=email, altura=altura, descricao=descricao, data_nascimento=data, telefone=telefone, imagem=imagem, ativo=True)
        novo_aluno.save()
        return redirect('home')
    else:
        return render(request, 'pages/adicionar.html')


def editar(request, id):
    aluno = Alunos.objects.get(id=id)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        matricula = request.POST.get('matricula')
        outras_info = request.POST.get('outras_info')
        data = request.POST.get('data_nasc')
        telefone = request.POST.get('telefone')
        imagem = request.FILES.get('imagem')
        
        if check == None:
            check = False
        else:
            check = True    
        imagem = request.FILES.get('imagem')
        print(imagem)
        aluno.nome = nome
        aluno.telefone = telefone
        aluno.data = data
        if imagem != None:
            aluno.imagem = imagem
        aluno.descricao = descricao
        aluno.save()
        return redirect('home')
    else:    
        return render(request, 'pages/editar.html', {'aluno':aluno})