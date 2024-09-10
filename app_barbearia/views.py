from django.shortcuts import render
from .models import Servico, Profissional

# Onde vai acontecer a lógica da aplicação, 
# consulta ao banco de dados, funções, renderização de páginas html

def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')


def servicos(request):
    context = {}
    lista_servicos = Servico.objects.all().order_by('categoria')
    context['lista_servicos'] = lista_servicos
    return render(request, 'servicos.html', context)

def profissionais(request):
    context = {}
    lista_profissionais = Profissional.objects.all()
    context['lista_profissionais'] = lista_profissionais
    return render(request, 'profissionais.html', context)

# def acesso(request):
#      return render(request, 'acessar.html')

# def usuario(request):
#     novo_usuario = Usuario()
#     novo_usuario.nome = request.POST.get('nome')
#     novo_usuario.nascimento = request.POST.get('nascimento')
#     novo_usuario.telefone = request.POST.get('telefone')
#     novo_usuario.email = request.POST.get('email')
#     novo_usuario.senha = request.POST.get('senha')
#     novo_usuario.save()
    
# def area_cliente(request):
#     return render(request,'area_cliente.html')
# def agenda(request):
#     return render(request, 'agenda.html', name='agenda')



# Servico.objects.create()