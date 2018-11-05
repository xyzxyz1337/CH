from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.postgres.search import SearchVector
from django.db.models import F

from .noteForm import createNoteForm
from blog.models import Post


def index(request):
    return render(request, 'index.html')


def edit(request, id):
    pass


def delete(request, id):
    try:
        post = Post.objects.get(id=id)
        post.delete()
        return HttpResponseRedirect("/")
    except Post.DoesNotExist:
        return HttpResponseNotFound("<h2>Post not found</h2>")


def search(request):

    if 'q' in request.GET and request.GET['q']:
        query = request.GET['q']

        try:
            results = Post.objects.annotate(search=SearchVector(
                'noteName', 'noteTags'),).filter(search=query)

            if results.count() is 0:
                return HttpResponse('По запросу {} мы искали, но ничего не нашли.'.format(query))

            # if request.COOKIE.get('id') == 1337:
            for result in results:
                view = Post.objects.get(noteName=result.noteName)
                view.noteCounter = F('noteCounter') + 1
                view.save()

            response = render(request, 'search.html', {'result': results})
            response.set_cookie(key='id', value=1337)

            return response

        except:
            return HttpResponse('По запросу {} мы искали, но ничего не нашли.'.format(query))

    return HttpResponseRedirect('/')


def createNote(request):
    if request.method == "POST":
        form = createNoteForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            tags = form.cleaned_data['tags']
            category = form.cleaned_data['category']

        Post.objects.bulk_create(
            [Post(noteName=title, noteText=text, noteCounter=0, noteTags=tags, noteCategory=category)])

        return HttpResponseRedirect('/')

    else:

        form = createNoteForm()
        return render(request, 'form-for-create-note.html', {'form': form})
