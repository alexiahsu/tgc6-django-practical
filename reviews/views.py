from django.shortcuts import render, HttpResponse, get_object_or_404
from .forms import ReviewForm, CommentForm
from books.models import Book
from .models import Review


# Create your views here.


def index(request):
    age = "24"
    gender = "female"
    return render(request, 'reviews/index.template.html', {
        'age': age,
        'gender': gender
    })

def create_review(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid:
            #form.save()

            #create a review based on the data in the form
            #but don't save to database yet
            review = form.save(commit=False)

            #fill in review's user id
            #request.user holds the user that is logged in

            #set the user of the review to be
            #the same as whichever use is logged in right now
            review.user = request.user

            #fill in which book the review is for
            review.book = book

            #save the review manually
            review.save()
            return HttpResponse("Review is created")
        else:
            return HttpResponse("Form has error")
    else:
        form = ReviewForm()
        return render(request, 'reviews/create_review.template.html', {
            'form': form,
            'book': book
        })

def create_comment(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.review = review
            comment.user = request.user
            comment.save()
            return HttpResponse("Comments created")
        else:
            return HttpResponse("Not valid")
    else:
        form = CommentForm()
        return render(request, 'reviews/create_comment.template.html', {
            'form': form,
            'review': review
        })
