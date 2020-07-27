from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.contrib import messages

from books.models import Book


# Create your views here.
def add_to_cart(request, book_id):

    # the cart object is a dictionary
    cart = request.session.get('shopping_cart', {})

    # check if the book_id I want to add already exists inside the cart already
    # if the book is not in the shopping cart
    if book_id not in cart:
        book = get_object_or_404(Book, pk=book_id)

        # add the book to cart
        cart[book_id] = {
            'id': book_id,
            'title': book.title,
            'cost': 99,
            'qty': 1
        }
    else:
        # if the book already exists in the cart
        cart[book_id]['qty'] += 1

    # save the shopping cart back to session
    request.session['shopping_cart'] = cart
    return HttpResponse("book added")


def view_cart(request):
    # loading the content of the 'shopping_cart' from the session
    cart = request.session['shopping_cart']
    return render(request, 'cart/view_cart.template.html', {
        "cart": cart
    })
