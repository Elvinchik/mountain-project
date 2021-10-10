from django.urls import path
from .views import zanzibar

urlpatterns = [
    path('zanzibar/', zanzibar)
]