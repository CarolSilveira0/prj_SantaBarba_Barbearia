"""
URL configuration for prj_SantaBarba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_barbearia import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('acessar/',views.acesso, name='acessar'),
    path('cliente/', views.area_cliente, name='area_cliente'),
    path('sobre/', views.sobre, name='sobre'),
    # path('servicos', views.login, name='login')
    # path('agenda', views.agenda, name='agenda'),
    # path('servicos', views.servicos, name='servicos')
]
