from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^books$', views.books),
    url(r'^authors_list', views.authors_list),
    url(r'^(?P<author_id>\d+)$', views.author_page)
]
