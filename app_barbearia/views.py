from django.shortcuts import render
# from .models import Usuario, Servico

# Onde vai acontecer a lógica da aplicação, 
# consulta ao banco de dados, funções, renderização de páginas html

def home(request):
    return render(request, 'home.html')

# def sobre(request):
#     return render(request, 'sobre.html')

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

# def profissionais(request):
#     return render(request, 'profissionais.html', name='profissionais')

# def servicos(request):
#     servicos = {
#         'servicos': Servico.objects.all()
#     }
    
    
#     return render(request, 'servicos.html', servicos)


# Servico.objects.create()