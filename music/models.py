from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Permission, User

# Create your models here.
# in the DB, the column name will be these attributes

class Album(models.Model):
    user = models.ForeignKey(User, default=1)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    # album_logo = models.CharField(max_length=1000)
    album_logo = models.FileField()
    is_favorite = models.BooleanField(default=False)

    # when we create a new album, a pk will be given, pk will be passed to primary view
    # whenever we use the view, we need to pass the pk
    # def get_absolute_url(self):
    #     return reverse('music:detail', kwargs={'pk': self.pk})

    # toString()
    def __str__(self):
        return self.album_title + " : " + self.artist

class Song(models.Model):

    # relates directly to the Album class, when Album is deleted, delete this song
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    # file_type = models.CharField(max_length=10)
    audio_file = models.FileField(default='')
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
