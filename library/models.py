from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField('Date of birth')

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Book(models.Model):
    title = models.CharField(max_length=50)
    page_number = models.IntegerField()
    genre = models.ManyToManyField(Genre)
    publishing_date = models.DateField('Date of publication')

    def __str__(self):
        return self.title
