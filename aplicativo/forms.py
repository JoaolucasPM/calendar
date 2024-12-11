from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ["nome","titulo", "descricao", "inicio", "fim"]
        widgets = {
            'inicio': forms.DateInput(attrs={'type': 'date'}),
            'fim': forms.DateInput(attrs={'type': 'date'}),
        }
