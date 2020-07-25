from django import forms
from .models import Book, Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # tuples are in ()
        fields = ('title', 'desc', 'ISBN', 'pageCount', 'genre', 'category', 'tag', 'authors', 'owner')

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'dob')