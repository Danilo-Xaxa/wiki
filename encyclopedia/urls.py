from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/random_page/", views.random_page, name="random_page"),
    path("wiki/search", views.search, name="search"),
    path("wiki/create_page/", views.create_page, name="create_page"),
    path("wiki/save_page/", views.save_page, name="save_page"),
    path("wiki/edit", views.edit, name="edit"),
    path("wiki/<str:title>", views.entry, name="entry"),
]
