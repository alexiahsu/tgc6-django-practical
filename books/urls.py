from django.contrib import admin
from django.urls import path, include
import books.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', books.views.index),
    path('all', books.views.show_books, name="all_books"),
    path('author', books.views.show_authors),
    path('create', books.views.create_book),
    path('author/create', books.views.create_author),
    path('update/<book_id>', books.views.edit_book,
         name="update_book_route"),
    path('author/<author_id>', books.views.edit_author,
         name="update_author"),
    path('delete/<book_id>', books.views.delete_book,
         name="delete_book"),
    path('details/<book_id>', books.views.view_book,
         name="view_book_details")
]
