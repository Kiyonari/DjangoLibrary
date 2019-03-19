from django import forms
from django_select2.forms import Select2MultipleWidget
from .models import Book


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'author': Select2MultipleWidget(),
            'genre': Select2MultipleWidget()
        }
