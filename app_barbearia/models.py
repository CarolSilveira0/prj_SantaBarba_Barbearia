
from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.forms.widgets import

LISTA_CATEGORIAS = (
    ('barba', 'Barba'),
    ('cabelo', 'Cabelo'),
    ('outro', 'Outros Serviços')    
)

# Create your models here.

class Servico(models.Model):
    codigo = models.CharField(max_length=6, unique=True)
    descricao_curta = models.CharField(max_length=50, default='descricao')
    descricao_longa = models.TextField(max_length=500, default='descricao longa')
    categoria = models.CharField(max_length=20, choices=LISTA_CATEGORIAS)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tempo = models.IntegerField()
    
    def __str__(self) -> str:
        return self.descricao_curta
    
    
class Profissional(models.Model):
    nome = models.CharField(max_length=250)
    foto = models.ImageField(upload_to='images')
    especialidade = models.CharField(max_length=20, choices=LISTA_CATEGORIAS)
    contato = models.CharField(max_length=20)
    historico = models.TextField(max_length=1000)
    
    def __str__(self) -> str:
        return self.nome


# class Agenda()

# class Usuario(AbstractUser):
#     data_nascimento = models.DateField()
    


# class AgendaAdmin(models.Manager):
#     """ Event manager """

#     def get_all_events(self, user):
#         events = Agenda.objects.filter(user=user, is_active=True, is_deleted=False)
#         return events

#     def get_running_events(self, user):
#         running_events = Agenda.objects.filter(
#             user=user,
#             is_active=True,
#             is_deleted=False,
#             end_time__gte=datetime.now().date(),
#         ).order_by("start_time")
#         return running_events


# class AgendaAbstrata(models.Model):
#     """ Event abstract model """

#     is_active = models.BooleanField(default=True)
#     is_deleted = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True
        
        
# class Agenda(AgendaAbstrata):
#     """ Event model """

#     user = models.ForeignKey("Usuario", related_name="usuarios")
#     profissional = models.ForeignKey("Profissional", related_name="profissionais")
#     servico = models.ManyToManyField("Servico")
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()

#     objects = AgendaAdmin()

#     def __str__(self):
#         return self.servico

#     def get_absolute_url(self):
#         return reverse("calendarapp:event-detail", args=(self.id,))

#     @property
#     def get_html_url(self):
#         url = reverse("calendarapp:event-detail", args=(self.id,))
#         return f'<a href="{url}"> {self.title} </a>'

   