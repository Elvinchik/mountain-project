from django.urls import path
from .views import maldivies

urlpatterns = [
    path("maldivies/", maldivies)
]