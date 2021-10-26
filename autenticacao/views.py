from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Cargos, Pessoa
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404
from django.shortcuts import redirect

def home(request):
    return redirect("/autenticacao/cadastro")

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro/index.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        pessoa = Pessoa(nome = nome,
                        email = email,
                        senha = senha
                        )

        pessoa.save()

        return HttpResponse('Você foi cadastrado')


def listar(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'listar/listar.html', {'pessoas': pessoas})

def listar_unico(request, id):
    pessoa = get_object_or_404(Pessoa, id = id)

    
    return render(request, 'listar/listar.html', {'pessoas': pessoa})
    