from django.shortcuts import render
from requisicao import Repositorio


def index(request):
    repositorios = Repositorio("ViniciusFebasse")
    colecoes = repositorios.requisita()

    return render(request, 'dados/index.html', {'colecoes': colecoes})