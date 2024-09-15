#Imports Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

#Imports projeto
from .models import Servico, Profissional, Agendamento, Usuario

#Adicionando campo de data de nascimento ao usuário para ser visto no admin do site
campos = list(UserAdmin.fieldsets)
campos.append(
    ("Histórico", {"fields":('data_nascimento',)})
    )
UserAdmin.fieldsets = tuple(campos)

#Campos para serem gerenciados no admin do site
admin.site.register(Servico)
admin.site.register(Profissional)
admin.site.register(Agendamento)
admin.site.register(Usuario, UserAdmin)
