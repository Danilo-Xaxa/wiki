from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/", views.random_page, name="random_page"),
    path("wiki/<str:title>", views.entry, name="entry"),
]
