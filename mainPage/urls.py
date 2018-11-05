from django.urls import path, re_path
from mainPage import views


urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    # ex: /create/
    path('create/', views.createNote, name='createNote'),
    # ex: /search/
    path('search/', views.search, name='search'),
    # ex: /search/delete/1332
    path('search/delete/<int:id>', views.delete, name='delete'),
    # ex: /search/edit/1332
    path('search/edit/<int:id>', views.edit, name='edit'),


]
