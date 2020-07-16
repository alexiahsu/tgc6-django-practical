from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Book, Author
from .forms import BookForm, AuthorForm

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

def create_book(request):
    #check if we are submitting the form
    if request.method == "POST":
        print(request.POST)
        # create the bookform by filling it with data from the user's submission
        form = BookForm(request.POST)
        form.save()
        #redirect back to show_books page
        return redirect(reverse(show_books))
    else:
    #create an instance of the class BookForm and store it in the form variable
        form = BookForm()
    return render(request, 'books/create_book.template.html', {
        'form': form
    })

def create_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        form.save()
        return redirect(reverse(show_authors))
    else:
        form = AuthorForm()
    return render(request, 'books/create_author.template.html', {
        'form': form
    })

