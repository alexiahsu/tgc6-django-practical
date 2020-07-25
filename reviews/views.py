from django.shortcuts import render, HttpResponse
from .forms import ReviewForm

# Create your views here.


def index(request):
    age = "24"
    gender = "female"
    return render(request, 'reviews/index.template.html', {
        'age': age,
        'gender': gender
    })

def create_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponse("Review is created")
        else:
            return HttpResponse("Form has error")
    else:
        form = ReviewForm()
        return render(request, 'reviews/create_review.template.html', {
            'form': form
        })

