from django.db import models

# Create your models here.

class Tag(models.Model):
    title = models.CharField(blank=False, max_length=255)
  
    def __str__(self):
        return self.title 

class Genre(models.Model):
    title = models.CharField(blank=False, max_length=255)
  
    def __str__(self):
        return self.title 

class Category(models.Model):
    title = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.title 


class Book(models.Model):
    title = models.CharField(blank=False, max_length=255)
    ISBN = models.CharField(blank=False, max_length=255)
    desc = models.TextField(blank=False)
    pageCount = models.IntegerField(blank=False)
    #relationship to genre - if genre gets deleted, book will be delete
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    authors = models.ManyToManyField('Author')

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(blank=False, max_length=80)
    last_name = models.CharField(blank=False, max_length=80)
    dob = models.DateField(blank=False)

    #gives the name of the object in django
    def __str__(self):
        return self.first_name + " " + self.last_name