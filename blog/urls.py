from django.urls import path
from blog import views

from mainPage import views as mainPage_view

urlpatterns = [
    path('', views.blog_page, name='blog_page'),
    path('delete/<int:id>/', mainPage_view.delete),
    path('edit/<int:id>/', mainPage_view.edit),
]
