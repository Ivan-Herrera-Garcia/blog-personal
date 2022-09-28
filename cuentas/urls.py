from urllib.parse import urlparse
from django.urls import path
from .views import VistaRegistro

urlpatterns = [
    path('registro/', VistaRegistro.as_view(), name = 'registro')

]