from django.db import models
from django.contrib.auth.models import User

# import the book model into this model
from books.models import Book

# Create your models here.


class Review(models.Model):
    title = models.CharField(max_length=255)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    # content of review is likely to be long, should use textfield insead
    content = models.TextField(blank=False)
    date = models.DateField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[0:50]
