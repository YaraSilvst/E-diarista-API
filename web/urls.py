from web.views import registrar_diarista
from django.urls import path
from .views import *

urlpatterns = [
    path('registrar_diarista/', registrar_diarista, name = 'diaristas'),
    path('editar-diarista/<int:diarista_id>', editar_diarista, name = "editar_diarista"),
    path('remover-diarista/<int:diarista_id>', remover_diarista, name = "remover_diarista"),
]