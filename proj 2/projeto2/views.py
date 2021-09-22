from django.shortcuts import render


def pagina_inicial(request):
    return render(request, 'home/pagina_inicial.html')
