from django.contrib import admin
# . refers to current directory 
from .models import Book

# Register your models here.
admin.site.register(Book)