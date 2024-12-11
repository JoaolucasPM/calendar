from django.db import models

from django.db import models

class Evento(models.Model):
    nome = models.CharField(max_length=200, default='teste')  # Nome do evento
    titulo = models.CharField(max_length=200)  # Nome do evento
    descricao = models.TextField(blank=True, null=True)  # Descrição opcional
    inicio = models.DateTimeField()  # Data e hora de início
    fim = models.DateTimeField(blank=True, null=True)  # Data e hora de término (opcional)
    criado_em = models.DateTimeField(auto_now_add=True)  # Data de criação
    atualizado_em = models.DateTimeField(auto_now=True)  # Última atualização

    def __str__(self):
        return self.titulo
