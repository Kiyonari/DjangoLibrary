from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField('Date of birth')

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ManyToManyField(Author)
    genre = models.ManyToManyField(Genre)
    page_number = models.IntegerField()
    publishing_date = models.DateField('Date of publication')
    front_cover = models.ImageField(default="./pictures/no-image-available.png")

    class Meta:
        ordering = ['publishing_date']

    def __str__(self):
        return self.title + ' (' + str(self.publishing_date.__format__("%Y")) + ')'
