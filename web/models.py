from django.db import models

class Diarista(models.Model):

    nome_completo = models.CharField(
        verbose_name = 'Nome Completo',
        max_length = 100,
    )

    cpf = models.CharField(
        verbose_name = 'CPF',
        max_length=11, 
        unique=True
    )

    email = models.EmailField(
        verbose_name = 'E-mail',
        unique=True
    )

    telefone = models.CharField(
        verbose_name = 'Telefone',
        max_length=11
    )

    logradouro = models.CharField(
        verbose_name = 'Logradouro',
        max_length=60
    )

    numero = models.IntegerField(
        verbose_name = 'Número',
    )

    bairro = models.CharField(
        verbose_name = 'Bairro',
        max_length=30
    )

    complemento = models.CharField(
        verbose_name = 'Complemento',
        max_length=100, 
        null=False, 
        blank=True
    )

    cep = models.CharField(
        verbose_name = 'CEP',
        max_length=8
    )

    estado = models.CharField(
        verbose_name = 'Estado',
        max_length=2
    )

    cidade = models.CharField(
        verbose_name = 'Cidade',
        max_length=30, 
        null=False, 
        blank=True
    )

    codigo_ibge = models.IntegerField(
        verbose_name = 'Código IBGE',
    )

    foto_usuario = models.ImageField(
        verbose_name = 'Foto Usuário',
        null=False
    )
