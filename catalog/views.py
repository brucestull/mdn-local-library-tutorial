from django.shortcuts import render

from .models import Author, Language, Genre, Book, BookInstance

def index(request):
    """
    View function for home/index page of site.
    """
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(
        status__exact='a',
    ).count()
    num_books_containing_the = Book.objects.filter(title__icontains='the').count()
    num_authors = Author.objects.count()
    num_genres = Genre.objects.count()
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_books_containing_the': num_books_containing_the,
        'num_authors': num_authors,
        'num_genres': num_genres,
    }
    return render(request, 'index.html', context=context)
