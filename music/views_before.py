from django.views import generic
from .models import Album
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.generic import View
from .forms import AlbumForm, UserForm, SongForm
from django.http import JsonResponse
from django.db.models import Q


AUDIO_FILE_TYPES = ['wav','mp3','ogg']
IMAGE_FILE_TYPES = ['png','jpg','jpeg']

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


class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    # display a blank form
    def get(self, request):
        form = self.form_class(None)   # no need to pass anything
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)     # always TRUE when valid data

        if form.is_valid():
            # creates object on the form, doesn't save to DB yet
            user = form.save(commit=False)

            # cleaned/normalized data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    # request.user     # to refer to the user
                    return redirect('music:index')

        # failed login, return to this form
        return render(request, self.template_name, {'form': form})

# def home(request):
#     return HttpResponse("HOMEPAGE<br/>HOST:" + request.get_host())




