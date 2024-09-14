from django.shortcuts import render
from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget
from .models import Servico, Profissional
# , Agenda
from django.views.generic import TemplateView, ListView

# Onde vai acontecer a lógica da aplicação, 
# consulta ao banco de dados, funções, renderização de páginas html

class Home(TemplateView):
    template_name = 'home.html'


class Sobre(TemplateView):
    template_name = 'sobre.html'


class Servicos(ListView):
    template_name = 'servicos.html'
    model = Servico  
    
# def servicos(request):
#     context = {}
#     lista_servicos = Servico.objects.all().order_by('categoria')
#     context['lista_servicos'] = lista_servicos
#     return render(request, 'servicos.html', context)

class Profissionais(ListView):
   template_name = 'profissionais.html'
   model = Profissional


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





 # def calcular_comissoes:
    # comissoes_Beatriz = []
    # for dia in agenda:
    #  agenda.valor * 0.70
    # if agenda.profissional == 'Beatriz':
        # comissoes_Beatriz.append(comissao)
        
    #return sum(comissoes_Beatriz)
    
    