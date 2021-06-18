
from django.shortcuts import render, redirect
from django.contrib import messages
from web.models import *
from web.forms import *

def registrar_diarista(request):

    form = DiaristaForm()

    if request.method == "POST":
        form = DiaristaForm(request.POST, request.FILES)

        if form.is_valid():
            diarista = form.save(commit=False)

            diarista.save()

            messages.success(request, "Diarista cadastrado com sucesso.")

            return redirect("listar_diarista")

    context = {
        "form": form
    }

    return render(request, "diaristas.html", context)

def listar_diaristas(request):

    diaristas = Diarista.objects.all()

    context = {
        "diaristas": diaristas
    }

    return render(request, "listar_diaristas.html", context)

def editar_diarista(request, diarista_id):

    diarista = Diarista.objects.get(id=diarista_id)

    if request.method == "POST":
        form = DiaristaForm(request.POST or None, request.FILES, instance=diarista)

        if form.is_valid():
            form.save()
            
            return redirect('listar_diarista')

    else: 
        form = DiaristaForm(instance=diarista)

    context = {
        "form": form
    }

    return render (request, 'diaristas.html', context)

def remover_diarista(request, diarista_id):

    diarista = Diarista.objects.get(id=diarista_id)
    diarista.delete()

    return redirect('listar_diarista')