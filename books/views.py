from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
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

def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        #the user has submitted data by extracting it from request.POST (content that user has posted)
        form = BookForm(request.POST, instance=book)
        form.save()
        return redirect(reverse(show_books))
    else:
    #retrieve the book that we want to edit
    #populate the form with the existing data from the book
        form = BookForm(instance=book)
    return render(request, 'books/edit_book.template.html', {
        'form': form
    })

def edit_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        form.save()
        return redirect(reverse(show_authors))
    else:
        form = AuthorForm(instance=author)
    return render(request, 'books/edit_author.template.html', {
        'form': form
    })

def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        book.delete()
        return redirect(reverse(show_books))
    else:
        return render(request, 'books/confirm_delete_book.template.html', {
            'book': book
        })

