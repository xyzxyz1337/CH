from django.urls import path, re_path
from blog import views

urlpatterns = [
    path('', views.blog_page, name='blog_page'),
]
