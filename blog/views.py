from django.shortcuts import render
from blog.models import Post


def blog_page(request):

    notes = Post.objects.all()
    return render(request, 'feed.html', {"notes": notes})
