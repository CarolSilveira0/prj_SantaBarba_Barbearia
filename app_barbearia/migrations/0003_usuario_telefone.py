# Generated by Django 5.1.1 on 2024-09-15 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_barbearia', '0002_agendamento_cancelado'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='telefone',
            field=models.CharField(default='0000', max_length=15),
        ),
    ]
