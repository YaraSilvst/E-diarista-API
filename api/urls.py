from django.urls import path
from api.views import *

urlpatterns = [
    path('diaristas-cidade/', DiaristasCidadeList.as_view(), name = 'diaristas_cidade'),
]