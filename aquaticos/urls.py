from django.urls import path
from . import views

app_name = 'aquaticos'

urlpatterns = [
    path('', views.views_index, name='index'),
]
