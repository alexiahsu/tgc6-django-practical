from django.shortcuts import render, HttpResponse

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
