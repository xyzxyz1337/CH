from django.shortcuts import render, HttpResponse
from blog.models import Post
from django.http import JsonResponse


def blog_page(request):

    notes = Post.objects.all()
    return render(request, 'feed.html', {"notes": notes})


def edit_post(request):
    post_title = request.GET.get('noteName')
    post_text = request.GET.get('noteText')
    post_tags = request.GET.get('noteTags')
