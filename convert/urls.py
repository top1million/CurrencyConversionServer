from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("convert", views.convert, name="convert"),
]
