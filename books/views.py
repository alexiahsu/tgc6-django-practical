from django.shortcuts import render, HttpResponse
from .models import Book, Author

# Create your views here.

# a view refers to a function
# that is called when its corresponding URL is visited in the browser

# all view functions must take in the variable request as the first argument


def index(request):
    fname = "Alexia"
    lname = "Hsu"
    return render(request, 'books/index.template.html', {
        'first_name': fname,
        'last_name': lname
    })

def show_books(request):
    # Select * from books
    all_books = Book.objects.all()
    #fetch all the objects
    return render(request, 'books/all_books.template.html', {
        'books': all_books
    })

def show_authors(request):
    all_authors = Author.objects.all()
    return render(request, 'books/authors.template.html', {
        'authors': all_authors
    })
