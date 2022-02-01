#from django.http import HttpResponse
from django.shortcuts import render
from animais.models import Animal


def index(request):
    context = {'caracteristicas': Animal.objects.all() }

    if 'buscar' in request.GET:
        animais = Animal.objects.all()
        animal_pesquisado = request.GET['buscar']
        caracteristicas_especificas = animais.filter(nome_animal__icontains = animal_pesquisado)
        context = {'caracteristicas': caracteristicas_especificas }
    return render(request, 'index.html', context)
    
