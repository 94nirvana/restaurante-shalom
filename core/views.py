from django.shortcuts import render
from django.contrib import messages
from .forms import ClienteModelForm, TransferenciaModelForm
from .forms import Cliente, Transferencia


def index(request):
    return render(request, 'index.html')


def fila(request):
    if str(request.method)=="POST":
        form = ClienteModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Dados enviados com sucesso!")
            form = ClienteModelForm()
        else:
            messages.error(request, "Erro ao salvar os dados!")
    else:
        form = ClienteModelForm()
    context = {
        'form': form,
        'clientes': Cliente.objects.all()
        }
    return render(request, 'fila.html', context)


def transferencia(request):
    if str(request.method) == "POST":
        form = TransferenciaModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Dados enviados com sucesso!")
            form = TransferenciaModelForm()
        else:
            messages.error(request, "Erro ao salvar os dados!")
    else:
        form = TransferenciaModelForm()
    context = {
            'form': form,
            'transferencias': Transferencia.objects.all()
        }
    return render(request, 'transferencia.html', context)

