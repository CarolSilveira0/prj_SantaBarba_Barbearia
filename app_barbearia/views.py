from django.shortcuts import render
from .models import Usuario, Servico

# Onde vai acontecer a lógica da aplicação, 
# consulta ao banco de dados, funções, renderização de páginas html

def home(requests):
    return render(requests, 'base.html')

def sobre(requests):
    return render(requests, 'sobre.html')

def acesso(requests):
     return render(requests, 'acessar.html')

def usuario(requests):
    novo_usuario = Usuario()
    novo_usuario.nome = requests.POST.get('nome')
    novo_usuario.nascimento = requests.POST.get('nascimento')
    novo_usuario.telefone = requests.POST.get('telefone')
    novo_usuario.email = requests.POST.get('email')
    novo_usuario.senha = requests.POST.get('senha')
    novo_usuario.save()
    
def area_cliente(requests):
    return render(requests,'area_cliente.html')
# def agenda(requests):
#     return render(requests, 'agenda.html', name='agenda')

# def profissionais(requests):
#     return render(requests, 'profissionais.html', name='profissionais')

def servicos(requests):
    servicos = {
        'servicos': Servico.objects.all()
    }
    
    
    return render(requests, 'servicos.html', servicos)


Servico.objects.create()