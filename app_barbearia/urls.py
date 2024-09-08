
from django.urls import path, include
from .views import home
# url - view - template

urlpatterns = [
    path('', home, name='home'),
    # path('acessar/',views.acesso, name='acessar'),
    # path('cliente/', views.area_cliente, name='area_cliente'),
    # path('sobre/', sobre, name='sobre'),
    # path('servicos', views.login, name='login')
    # path('agenda', views.agenda, name='agenda'),
    # path('servicos', views.servicos, name='servicos')  
]
    
    
    