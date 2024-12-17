from django.urls import path
from . import views


urlpatterns = [
    # URLs funcionais
    path('', views.app_index, name='app_index'),
    path('agenda/', views.app_agenda, name='app_agenda'),
    path('global/', views.global_pag, name='global_pag'),

    # URLs baseadas em classe
    path('eventos/', views.ProductListView.as_view(), name='listView'),
    path('evento/create/', views.ProductCreateView.as_view(), name='createView'),
    path('evento/<pk>/edit/', views.EventoUpdateView.as_view(), name='updateView'),
    path('evento/<pk>/delete/', views.ProductDeleteView.as_view(), name='deleteView'),

    # URL para eventos em formato JSON
    path('api/eventos/', views.eventos, name='eventos_json'),
]