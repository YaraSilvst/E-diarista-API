# Generated by Django 3.1.12 on 2021-06-16 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diarista',
            name='bairro',
            field=models.CharField(max_length=30, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='diarista',
            name='cep',
            field=models.CharField(max_length=8, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='diarista',
            name='cidade',
            field=models.CharField(blank=True, max_length=30, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='diarista',
            name='codigo_ibge',
            field=models.IntegerField(verbose_name='Código IBGE'),
        ),
        migrations.AlterField(
            model_name='diarista',
            name='complemento',
            field=models.CharField(blank=True, max_length=100, verbose_name='Complemento'),
        ),
        migrations.AlterField(
            model_name='diarista',
            name='cpf',
            field=models.CharField(max_length=11, unique=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='diarista',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='diarista',
            name='estado',
            field=models.CharField(max_length=2, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='diarista',
            name='foto_usuario',
            field=models.ImageField(upload_to='', verbose_name='Foto Usuário'),
        ),
        migrations.AlterField(
            model_name='diarista',
            name='logradouro',
            field=models.CharField(max_length=60, verbose_name='Logradouro'),
        ),
        migrations.AlterField(
            model_name='diarista',
            name='nome_completo',
            field=models.CharField(max_length=100, verbose_name='Nome Completo'),
        ),
        migrations.AlterField(
            model_name='diarista',
            name='numero',
            field=models.IntegerField(verbose_name='Número'),
        ),
        migrations.AlterField(
            model_name='diarista',
            name='telefone',
            field=models.CharField(max_length=11, verbose_name='Telefone'),
        ),
    ]
