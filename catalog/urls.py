from django.urls import path

from . import views

app_name='catalog'
urlpatterns = [
    path(
        '',
        views.index,
        name='index'
    ),

    path(
        'books/',
        views.BookListView.as_view(),
        name='books'
    ),
    path(
        'books/<int:pk>/',
        views.BookDetailView.as_view(),
        name='book-detail'
    ),
    path(
        'books/<int:pk>/update/',
        views.BookUpdate.as_view(),
        name='book-update'
    ),
    path(
        'books/<int:pk>/delete/',
        views.BookDelete.as_view(),
        name='book-delete'
    ),

    path(
        'authors/',
        views.AuthorListView.as_view(),
        name='authors'
    ),
    path(
        'authors/<int:pk>/',
        views.AuthorDetailView.as_view(),
        name='author-detail'
    ),
    path(
        'authors/create/',
        views.AuthorCreate.as_view(),
        name='author-create'
    ),
    path(
        'authors/<int:pk>/update/',
        views.AuthorUpdate.as_view(),
        name='author-update'
    ),
    path(
        'authors/<int:pk>/delete/',
        views.AuthorDelete.as_view(),
        name='author-delete'
    ),

    path(
        'mybooks/',
        views.LoanedBooksByUserListView.as_view(),
        name='my-borrowed'
    ),
    path(
        'borrowed/',
        views.LoanedBooksAllListView.as_view(),
        name='all-borrowed'
    ),

    path(
        'book/<uuid:pk>/renew/',
        views.renew_book_librarian,
        name='renew-book-librarian'
    ),
]