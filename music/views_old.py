# from django.shortcuts import render
# from django.template import loader

from .models import Album
from django.shortcuts import render, get_object_or_404
# from django.http import Http404

# Create your views here.
from django.http import HttpResponse


def index(request):
    # save all Albums in a variable
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', {'all_albums': all_albums})

    # template = loader.get_template('music/index.html')
    # pass this info to our template
    #return HttpResponse(template.render(context, request))
    # shorten and combine

    '''
    for album in all_albums:
        # build link
        url = "/music/" + str(album.id) + '/'
        html += '<a href=" ' +  url  + ' ">' + album.album_title + '</a><br/>'
    # return HttpResponse("<h1>This is the music app homepage<h1>")

    return HttpResponse(html)
    '''


def detail(request, album_id):
    # return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2>")

    # try:
    #     album = Album.objects.get(pk=album_id)
    # except Album.DoesNotExist:
    #     raise Http404("Album does not exist")

    album = get_object_or_404(Album, pk=album_id)

    return render(request, 'music/detail.html', {'album': album})


# function to catch localhost:8000 aka homepage
def home(request):
    return HttpResponse("HOMEPAGE<br/>HOST:" + request.get_host())
