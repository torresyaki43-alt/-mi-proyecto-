# saludos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Esta URL manejará tanto la visualización del formulario (GET) como el envío (POST)
    path('', views.generador_carta, name='generador_carta'),
]