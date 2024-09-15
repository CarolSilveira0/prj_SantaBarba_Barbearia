#Imports Django
from django.urls import path
from django.contrib.auth import views as auth_view

#Imports Projeto
from .views import Home,Sobre, Servicos, Profissionais, AgendaFormView, AreaCliente, Historico, cancelar_agendamento, CriarContaFormView, EditarConta

# Estrutura: url - view - template

#Nome do app que iremos utilizar nas urls
app_name = 'barbearia'

#Urls do site
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('sobre/', Sobre.as_view(), name='sobre'),
    path('servicos/', Servicos.as_view(), name='servicos'),
    path('profissionais/', Profissionais.as_view(), name='profissionais'), 
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('login/criar_conta/', CriarContaFormView.as_view(), name='criar_conta'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html', next_page='barbearia:login'), name='logout'),
    path('area_cliente/', AreaCliente.as_view(), name='area_cliente_home'),
    path('area_cliente/agenda/', AgendaFormView.as_view(), name='agendar'),
    path('area_cliente/historico/', Historico.as_view(), name='historico'),
    path('cancelar_agendamento/<int:agendamento_id>/', cancelar_agendamento, name='cancelar_agendamento'),
    path('area_cliente/editar_cadastro/<int:pk>', EditarConta.as_view(), name='edit_conta'),
    
]
    
    
    