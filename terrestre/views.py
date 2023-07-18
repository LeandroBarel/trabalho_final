from django.shortcuts import render

def views_index(request):
    return render(request, 'terrestre/paginas/index.html')
