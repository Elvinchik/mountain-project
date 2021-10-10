from django.urls import path
from .views import bali

urlpatterns = [
    path('bali/', bali)
]