from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    age = "24"
    gender = "female"
    return render(request, 'reviews/index.template.html', {
        'age': age,
        'gender': gender
    })
