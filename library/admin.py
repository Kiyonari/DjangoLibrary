from django.contrib import admin
import django.contrib.auth.admin
import django.contrib.auth.models
from django.contrib import auth

from library.form import BookForm
from .models import Author, Book, Genre


class GenreAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


class BookAdmin(admin.ModelAdmin):
    form = BookForm


admin.site.register(Author)
admin.site.register(Book, BookAdmin)
admin.site.register(Genre, GenreAdmin)

admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)
