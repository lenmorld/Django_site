from django.contrib import admin
from .models import Album, Song

# to be able to manage DB tables from localhost:8000/admin
from .models import Album

# enable these objects to be managed in Admin
admin.site.register(Album)
admin.site.register(Song)


# Register your models here.
