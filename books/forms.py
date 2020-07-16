from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # tuples are in ()
        fields = ('title', 'desc', 'ISBN', 'pageCount')