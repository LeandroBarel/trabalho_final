from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
<<<<<<< HEAD
    path('', views.views_home, name='index'),
=======
    path('', views.views_home, name='home'),
>>>>>>> 41aa8c8eba23b1eefd1978d22017e7db5f801d87
]
