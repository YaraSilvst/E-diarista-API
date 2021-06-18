from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from api.service.cidades_atendimento_service import listar_diaristas_cidade
from api.serializer import diaristas_cidade_serializer
from api.pagination import diaristas_cidade_pagination

class DiaristasCidadeList(APIView, diaristas_cidade_pagination.DiaristasCidadePagination):

    def get(self, request, format = None):

        cep = self.request.query_params.get('cep', None)

        diaristas = listar_diaristas_cidade(cep)
        resultado = self.paginate_queryset(diaristas, request)
        context = {
            "request": request
        }
        serializer = diaristas_cidade_serializer.DiaristaCidadeSerializer(resultado, many = True, context = context)
        

        return self.get_paginated_response(serializer.data)