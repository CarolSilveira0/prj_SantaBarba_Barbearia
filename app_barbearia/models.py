from django.db import models

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
# class Agenda

    # def calcular_comissoes:
    # comissoes_Beatriz = []
    # for dia in agenda:
    #  agenda.valor * 0.70
    # if agenda.profissional == 'Beatriz':
        # comissoes_Beatriz.append(comissao)
        
    #return sum(comissoes_Beatriz)
    
    