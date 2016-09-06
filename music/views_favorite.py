from .models import Album
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse

def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', {'all_albums': all_albums})


def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})

def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html',  {
            'album': album,
            'error_message' : "You did not select a valid song", })
    else:
        selected_song.is_favorite = True
        selected_song.save()    # store changes to DB
        return render(request, 'music/detail.html', {'album': album})

# function to catch localhost:8000 aka homepage
def home(request):
    return HttpResponse("HOMEPAGE<br/>HOST:" + request.get_host())
