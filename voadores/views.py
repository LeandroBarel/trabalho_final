from django.shortcuts import render

def views_index(request):
    return render(request, 'voadores/paginas/index.html')
