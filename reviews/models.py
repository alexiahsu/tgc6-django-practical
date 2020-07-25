from django.db import models

# import the book model into this model
from books.models import Book

# Create your models here.


class Review(models.Model):
    title = models.CharField(max_length=255)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    # content of review is likely to be long, should use textfield insead
    content = models.TextField(blank=False)
    date = models.DateField(blank=False)

    def __str__(self):
        return self.title
