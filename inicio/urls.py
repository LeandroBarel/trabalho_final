from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# app_name = 'home'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('terrestre/', include('terrestre.urls')),
    path('aquaticos/', include('aquaticos.urls')),
    path('voadores/', include('voadores.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
