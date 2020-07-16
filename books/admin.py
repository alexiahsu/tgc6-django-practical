from django.contrib import admin
# . refers to current directory 
from .models import Book, Author

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)