from django.urls import path, re_path
from mainPage import views

urlpatterns = [
    path('', views.root, name='root'),
    path('create/', views.createNote, name='createNote'),
    path('search/', views.search, name='search'),
    path('search/delete/<int:id>/', views.delete),
    path('search/edit/<int:id>/', views.edit),
]
