from django.urls import path
from .views import borabora

urlpatterns = [
    path('borabora/', borabora),
]