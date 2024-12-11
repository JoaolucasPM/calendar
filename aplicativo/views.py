from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import Evento
from django.shortcuts import render
from .forms import EventoForm
from django.utils.timezone import now



def global_pag(request):
    return render(request, 'pages/global.html')

class ProductListView(ListView):
    model = Evento
    template_name = 'app_listView.html'
    context_object_name = 'Event'

    # Filtro personalizado
    def get_queryset(self):
        queryset = super().get_queryset()
        start_date = now().date()  # Obtém apenas a data (ano, mês, dia)
        if start_date:
            queryset = queryset.filter(criado_em__date__gte=start_date) 
           
        return queryset
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['count_len'] = self.get_queryset().count()
        return context
    
class ProductCreateView(CreateView):
    model = Evento
    template_name = 'app_form.html'  
    form_class  = EventoForm
    success_url = reverse_lazy("listView")

def eventos(request):
    eventos = Evento.objects.all()
    eventos_list = [
        {
            "title": evento.titulo,
            "start": evento.inicio.isoformat(),
            "end": evento.fim.isoformat() if evento.fim else None,
        }
        for evento in eventos
    ]
    return JsonResponse(eventos_list, safe=False)



def app_agenda(request):
    return render(request, 'app_agenda.html')

def app_index(request):
    return render(request, 'app_index.html')

def app_index(request):
    return render(request, 'app_index.html')

class ProductDeleteView(DeleteView):
    model = Evento
    success_url = reverse_lazy("listView")


class EventoUpdateView(UpdateView):
    model = Evento
    fields = ["nome", "titulo", "descricao", "inicio", "fim"]
    template_name = "app_edit.html"
    success_url = reverse_lazy("listView")  
