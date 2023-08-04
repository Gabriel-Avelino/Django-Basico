from django.shortcuts import render
from django.http import HttpResponse


def ver_produto(request):
    nome = 'Gabriel'
    return render(request, 'ver_produto.html', {'nome': nome})  # Request, <nome_do_html>, context = {dados}


def inserir_produto(request):
    return HttpResponse('Estou no inserir')