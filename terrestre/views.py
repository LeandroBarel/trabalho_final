from django.shortcuts import render


def view_index(request):
    return render(request, 'terrestre/paginas/index.html')
