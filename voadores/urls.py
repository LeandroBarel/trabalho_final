from django.urls import path
from . import views

app_name = 'voadores'

urlpatterns = [
    path('', views.views_index, name='index'),
]
