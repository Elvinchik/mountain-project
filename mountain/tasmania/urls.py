from django.urls import path
from .views import tasmania

urlpatterns = [
    path('tasmania/', tasmania)
]