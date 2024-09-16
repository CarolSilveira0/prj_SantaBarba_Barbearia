
from datetime import date, datetime, timedelta
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User, AbstractUser

#Onde criamos as tabelas e lógica do banco de dados

#Lista de categorias usada pela tabela Servico
LISTA_CATEGORIAS = (
    ('barba', 'Barba'),
    ('cabelo', 'Cabelo'),
    ('outro', 'Outros Serviços')    
)

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
    
    def is_available(self, data, hora_inicio, duracao):
        """
        Verifica se o profissional está disponível para um serviço."""

       # Converter hora_inicio para datetime
        hora_inicio_dt = datetime.combine(data, hora_inicio)
        # Calcular o horário de término do agendamento
        hora_fim_dt = hora_inicio_dt + timedelta(minutes=duracao)

        # Verificar se existem agendamentos conflitantes para o profissional
        agendamentos_conflitantes = Agendamento.objects.filter(
            Q(hora_inicio__range=(hora_inicio_dt.time(), hora_fim_dt.time())) | 
            Q(hora_fim__range=(hora_inicio_dt.time(), hora_fim_dt.time())),
            profissional=self,
            data=data
        )

        return not agendamentos_conflitantes.exists()
 
    
class Usuario(AbstractUser):
    data_nascimento = models.DateField(blank=True, null=True)
    telefone = models.CharField(max_length=15, default='0000')
    
    
class Agendamento(models.Model):
    nome_usuario = models.ForeignKey(Usuario, related_name="agendamentos", on_delete=models.CASCADE)
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField(blank=True, null=True)
    servico = models.ForeignKey("Servico", on_delete=models.CASCADE)
    profissional = models.ForeignKey("Profissional", on_delete=models.CASCADE)
    valor_servico = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cancelado = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.hora_inicio and self.servico:
            self.hora_fim = (datetime.combine(date.today(), self.hora_inicio) + timedelta(minutes=self.servico.tempo)).time()
            self.valor_servico = self.servico.valor
        super().save(*args, **kwargs)

    def __str__(self):
        data_formatada = self.data.strftime("%d/%m/%Y")
        return f"{self.nome_usuario} - {self.servico} com {self.profissional} em {data_formatada} às {self.hora_inicio} - valor a pagar R${self.valor_servico}"