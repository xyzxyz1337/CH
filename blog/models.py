from django.db import models


class Post(models.Model):
    """In context name,text,couter,
       tags,category"""

    def __str__(self):
        return self.noteName

    categoryPost = [
        ('Note', 'Note'),
        ('Quest', 'Question'),
    ]

    noteName = models.CharField(
        max_length=40, unique=True, verbose_name='Заголовок')
    noteText = models.CharField(max_length=500, verbose_name='Текст')
    noteCounter = models.PositiveIntegerField(
        default=0, verbose_name='Количество просмотров')
    datePublished = models.DateTimeField(
        auto_now_add=True, verbose_name='Date published')
    dateModified = models.DateTimeField(
        auto_now=True, verbose_name='Date modified')
    noteTags = models.CharField(
        max_length=30, default=None, blank=True, verbose_name='Теги')
    noteCategory = models.CharField(
        choices=categoryPost, max_length=5, default='Note', verbose_name='Категория')
