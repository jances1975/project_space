from django.shortcuts import render, redirect, HttpResponse
from apps.usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
# importação de auth / User para verificar dados de usuários
from django.contrib import auth
# Adicionando mensagens de erro ao Django - messages
from django.contrib import messages


def login(request):
    form = LoginForms()

    if request.method == "POST":
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form["nome_login"].value()
            senha = form["senha"].value()

        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )
        # se Any deu certo se None a autenticação não deu certo
        if usuario is not None:
            auth.login(request, usuario)
            # aqui está fazendo o login (usuário e senha como parametro)
            messages.success(request, f"{nome} logado com Sucesso!")
            return redirect("index")
            # caso tenha logado voltar a página principal
        else:
            messages.error(request, "Erro ao efetuar login!")
            return redirect("login")
            # volta para tela de login caso não dê certo

    return render(request, "usuarios/login.html", {"form": form})
    # dicioanrio {"key": form(variavel)}


def cadastro(request):
    form = CadastroForms()

    if request.method == "POST":
        form = CadastroForms(request.POST)

        if form.is_valid():
            nome = form["nome_cadastro"].value()
            email = form["email"].value()
            senha = form["senha_1"].value()
            # username é campo da tabela User
            if User.objects.filter(username=nome).exists():
                messages.error(
                    request, "Esse nome de usuário já existe, use outro nome.")
                return redirect("cadastro")

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, f"{nome} cadastrado com sucesso!")
            return redirect("login")

    return render(request, "usuarios/cadastro.html", {"form": form})


def logout(request):
    auth.logout(request)
    messages.success(request, "Usuário deslogou com sucesso!")
    return redirect("login")
