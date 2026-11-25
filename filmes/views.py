
from django.shortcuts import render
from .models import Filme, Diretor, Categoria
from django.core.paginator import Paginator

def lista_filmes(request):

    pesquisa = request.GET.get('q', '')
    diretor = request.GET.get('diretor', '')
    categoria = request.GET.get('categoria', '')

    filmes = Filme.objects.all()

    if pesquisa:
        filmes = filmes.filter(
            titulo__icontains=pesquisa
        )

    if diretor:
        filmes = filmes.filter(
            diretor_id=diretor
        )


    if categoria:
        filmes = filmes.filter(
            categoria_id=categoria
        )

    contexto = {
        'filmes': filmes,
        'diretores': Diretor.objects.all(),
        'categorias': Categoria.objects.all(),
        'pesquisa': pesquisa,
        'diretor_selecionado': diretor,
        'categoria_selecionada': categoria,
    }

    return render(request, 'filmes/lista.html', contexto)
