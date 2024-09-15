#Imports Django e outros
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms


#Imports Projeto e externos
from datetime import timedelta, date, datetime
from .models import Agendamento, Usuario

#Classes dos formulários - fazem ligação com o banco de dados e constroem a lógica dessa ligação
class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['data', 'hora_inicio', 'servico', 'profissional', 'valor_servico']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date', 'min': date.today().strftime('%Y-%m-%d')}),
            'hora_inicio': forms.TimeInput(attrs={'type': 'time', 'step': '1800', 'id': 'hora_inicio'}),  # exibe o tempo de 30 em 30 minutos
            'valor_servico': forms.TextInput(attrs={'readonly': 'true'})
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['valor_servico'].initial = self.instance.servico.valor
            self.fields['valor_servico'].disabled = True
            
    def clean(self):
        cleaned_data = super().clean()
        hora_inicio = cleaned_data.get('hora_inicio')
        servico = cleaned_data.get('servico')
        profissional = cleaned_data.get('profissional')
        data = cleaned_data.get('data')

        # Verificar se o profissional está disponível no horário e data escolhidos
        if profissional and not profissional.is_available(data, hora_inicio, servico.tempo):
            raise forms.ValidationError("O profissional não está disponível neste horário.")

        # Calcular o horário de término e verificar se há outros agendamentos conflitantes
        hora_inicio_dt = datetime.combine(data, hora_inicio)
        hora_fim_dt = hora_inicio_dt + timedelta(minutes=servico.tempo)
        if Agendamento.objects.filter(profissional=profissional, data=data,
                                       hora_inicio__range=(hora_inicio_dt.time(), hora_fim_dt.time())).exists():
            raise forms.ValidationError("Já existe um agendamento neste horário.")
        # Definir o valor do serviço
        cleaned_data['valor_servico'] = servico.valor
        
        return cleaned_data
    
    def save(self, commit=True):
        agendamento = super().save(commit=False)
        if self.user:
            agendamento.nome_usuario = self.user
        if commit:
            agendamento.save()
        return agendamento


class CriarContaForm(UserCreationForm):
    email = forms.EmailField()
    telefone = forms.CharField()
    data_nascimento = forms.DateField(
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'placeholder': 'dd/mm/aaaa'})
    )    
    
    class Meta:
        model = Usuario
        fields = ('username', 'first_name', 'last_name', 'email', 'telefone', 'data_nascimento','password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data_nascimento'].input_formats = ['%d/%m/%Y']
        

