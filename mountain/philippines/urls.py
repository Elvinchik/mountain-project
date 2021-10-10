from django.urls import path
from .views import philippines

urlpatterns = [
    path('philippines/', philippines)
]