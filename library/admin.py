from django.contrib import admin
from django.contrib.auth.models import User, Group

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

admin.site.unregister(User)
admin.site.unregister(Group)
