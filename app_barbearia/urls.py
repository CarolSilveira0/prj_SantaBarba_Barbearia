
from django.urls import path, include
from .views import home,sobre, servicos, profissionais
# url - view - template

urlpatterns = [
    path('', home, name='home'),
    path('sobre/', sobre, name='sobre'),
    path('servicos/', servicos, name='servicos'),
    path('profissionais/', profissionais, name='profissionais'), 
    # path('acessar/',views.acesso, name='acessar'),
    # path('cliente/', views.area_cliente, name='area_cliente'),
    # path('agenda', views.agenda, name='agenda'),
]
    
    
    