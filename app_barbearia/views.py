#Imports do django
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import TemplateView, ListView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, reverse
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.utils.timezone import now

#Imports do projeto
from .forms import AgendaForm, CriarContaForm
from .models import Servico, Profissional, Agendamento, Usuario

# Onde vai acontecer a lógica da aplicação: consulta ao banco de dados, funções, renderização de páginas html

class Home(TemplateView):
    template_name = 'home.html'


class Sobre(TemplateView):
    template_name = 'sobre.html'


class Servicos(ListView):
    template_name = 'servicos.html'
    model = Servico  
    

class Profissionais(ListView):
   template_name = 'profissionais.html'
   model = Profissional
        
    
class AgendaFormView(LoginRequiredMixin, FormView):
    template_name = 'agenda.html'
    form_class = AgendaForm
    success_url = reverse_lazy('barbearia:area_cliente_home')

    def form_valid(self, form):
        agendamento = form.save(commit=False)
        agendamento.valor_servico = form.cleaned_data['valor_servico']
        agendamento.nome_usuario = self.request.user  # Atribui o usuário logado ao agendamento
        messages.success(self.request, 'Agendamento realizado com sucesso!')
        agendamento.save()
        return render(self.request, 'area_cliente_home.html', {'message': 'Agendamento realizado com sucesso!'})

    
class AreaCliente(LoginRequiredMixin, TemplateView):
    template_name = 'area_cliente_home.html'

    
class Historico(LoginRequiredMixin, ListView):
    template_name = 'historico.html'
    model = Agendamento
    context_object_name = 'agendamentos'

    def get_queryset(self):
        return Agendamento.objects.filter(nome_usuario=self.request.user).order_by('-data')[:5]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = now().date()
        return context
 
    
def cancelar_agendamento(request, agendamento_id):
    agendamento = get_object_or_404(Agendamento, id=agendamento_id)
    if agendamento.data > now().date():  # Verifica se o agendamento é futuro
        agendamento.cancelado = True
        agendamento.save()
        messages.success(request, 'Agendamento cancelado com sucesso.')
    else:
        messages.error(request, 'Não é possível cancelar agendamentos passados.')
    return redirect('barbearia:historico')


class EditarCadastro(LoginRequiredMixin, TemplateView):
    template_name = 'edit_cadastro.html'
    

class CriarContaFormView(FormView):
    template_name = 'criar_conta.html'
    form_class = CriarContaForm
    success_url = reverse_lazy('barbearia:login')  # Redireciona para a página de login após o cadastro

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    
class EditarConta(LoginRequiredMixin, UpdateView):
    template_name = 'edit_cadastro.html'
    model = Usuario
    fields = ['username', 'email', 'telefone']

    def get_success_url(self) -> str:
        return reverse('barbearia:area_cliente_home')