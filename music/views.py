from django.views import generic
from .models import Album
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

# 2 generic views, 1 list, 1 details

class IndexView(generic.ListView):
    template_name = 'music/index.html'  # whenever we get a list of albums, plug it here
    context_object_name = 'object_list'  # we can change this

    def get_queryset(self):     # query DB for whatever album we want, this ex. get all
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    model = Album
    # fields that we'll allow user to fill out
    # we can write a crawler that gets logo atuomatically, or fill the genre
    # for now, we allow user to type everything
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


# def home(request):
#     return HttpResponse("HOMEPAGE<br/>HOST:" + request.get_host())




