from django.urls import path, re_path
from blog import views

from mainPage import views as mainPage_view

urlpatterns = [
    path('', views.blog_page, name='blog_page'),
    # path('delete', mainPage_view.delete, name='delete'),
    # path('edit', mainPage_view.edit, name='edit'),
]
