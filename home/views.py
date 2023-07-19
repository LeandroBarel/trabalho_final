from django.shortcuts import render


def view_home(request):
    return render(request, 'paginas/index_home.html')
