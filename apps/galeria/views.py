from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
# from django.http import HttpResponse
from apps.galeria.models import Fotografia
# importando a models(tabela Fotografia) da galeria
from django.contrib import messages


def filtrarnebulosa(request):
    fotografia = Fotografia.objects.all().filter(categoria__icontains="NEBULOSA")
    return render(request, "galeria/index.html", {"cards": fotografia})


def filtrarestrela(request):
    fotografia = Fotografia.objects.all().filter(categoria__icontains="ESTRELA")
    return render(request, "galeria/index.html", {"cards": fotografia})


def filtrarplaneta(request):
    fotografia = Fotografia.objects.all().filter(categoria__icontains="PLANETA")
    return render(request, "galeria/index.html", {"cards": fotografia})


def filtrargalaxia(request):
    fotografia = Fotografia.objects.all().filter(categoria__icontains="GALAXIA")
    return render(request, "galeria/index.html", {"cards": fotografia})


def index(request):
    # Caso não esteja logado não poderá entrar na página index e será
    # redirecionado para tela de login
    if not request.user.is_authenticated:
        messages.error(
            request, "È necessário logar para ter acesso a galeria!")
        return redirect("login")

    fotografia = Fotografia.objects.order_by("nome").filter(publicada=True)
    # ou em ordem invertida
    # fotografia = Fotografia.objects.order_by("-nome").filter(publicada=True)
    # fotografia = Fotografia.objects.all()
    # a variavel fotografias recebendo todo o conteudo da tabela Fotografia

    # dados = {
    #    1: {"nome":"Nebulosa de Carina",
    #        "legenda":"webbtelescope.org / NASA / James Webb"},
    #    2: {"nome":"Galáxia NGC 1079",
    #        "legenda":"nasa.org / NASA / Hubble"}
    # }

    # Enviando o dic dados com nome cards (anterior)
    # Enviando a variavel fotografias com todo o conteudo da tabela Fotografia com nome cards (atual) para index.html
    return render(request, "galeria/index.html", {"cards": fotografia})
    # return render(request, "index.html") (anterior)
    # return HttpResponse('<h1>Projeto Space</h1><p>Bem vindo ao Espaço</p>') (anterior)


def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})


def buscar(request):
    if not request.user.is_authenticated:
        messages.error(
            request, "Você deve está logado para pesquisar na galeria!")
        return redirect("login")

    fotografias = Fotografia.objects.order_by("nome").filter(publicada=True)

    # esse buscar vem do link da caixa de pesquisa
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(
                categoria__icontains=nome_a_buscar)
            # nome__icontains tipo filtar por qualquer parte do campo *campo ou campo*
    return render(request, "galeria/buscar.html", {"cards": fotografias})


def nova_imagem(request):
    return render(request, "galeria/nova_imagem.html")


def editar_imagem(request):
    return render(request, "galeria/editar_imagem.html")


def deletar_imagem(request):
    return render(request, "galeria/deletar_imagem.html")
