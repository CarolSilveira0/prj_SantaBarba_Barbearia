
from django.urls import path, include
from .views import Home,Sobre, Servicos, Profissionais
# , Agenda
# url - view - template

app_name = 'barbearia'


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('sobre/', Sobre.as_view(), name='sobre'),
    path('servicos/', Servicos.as_view(), name='servicos'),
    path('profissionais/', Profissionais.as_view(), name='profissionais'), 
    # path('area_cliente/login',Login.as_view(), name='login'),
    # path('area_cliente/cliente/', views.area_cliente, name='area_cliente'),
    # path('area_cliente/agenda/', Agenda.as_view(), name='agenda'),
]
    
    
    