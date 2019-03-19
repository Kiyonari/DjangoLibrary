from django.http import HttpResponse
from django.template import loader

from library.models import Author
from .models import Book


def index(request):
    return HttpResponse("Hello World")


def books(request):
    books_list = Book.objects.all()
    template = loader.get_template('library/books.html')
    context = {'books': books_list}
    return HttpResponse(template.render(context, request))


def authors_list(request):
    authors_list = Author.objects.all()
    template = loader.get_template('library/authors_list.html')
    context = {'authors_list': authors_list}
    return HttpResponse(template.render(context, request))


def author_page(request, author_id):
    author = Author.objects.get(pk=author_id)
    books_list = Book.objects.all()
    template = loader.get_template('library/author_page.html')
    context = {
        'author': author,
        'books': books_list
       }
    return HttpResponse(template.render(context, request))
