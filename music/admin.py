from django.contrib import admin


# to be able to manage DB tables from localhost:8000/admin
from .models import Album

admin.site.register(Album)


# Register your models here.
