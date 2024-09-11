
from django.urls import path, include
from .views import Home,Sobre, Servicos, Profissionais
# url - view - template

app_name = 'barbearia'


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('sobre/', Sobre.as_view(), name='sobre'),
    path('servicos/', Servicos.as_view(), name='servicos'),
    path('profissionais/', Profissionais.as_view(), name='profissionais'), 
    # path('acessar/',views.acesso, name='acessar'),
    # path('cliente/', views.area_cliente, name='area_cliente'),
    # path('agenda', views.agenda, name='agenda'),
]
    
    
    