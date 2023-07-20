from django.shortcuts import render


def views_home(request):
    return render(request, 'paginas/index_home.html')
