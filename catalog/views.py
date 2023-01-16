from django.shortcuts import render
from django.views.generic import ListView, DetailView

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
    num_books_containing_the = Book.objects.filter(
        title__icontains='the'
    ).count()
    num_authors = Author.objects.count()
    num_genres = Genre.objects.count()

    # Session change:
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_books_containing_the': num_books_containing_the,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_visits': num_visits,
    }
    return render(request, 'index.html', context=context)


class BookListView(ListView):
    model = Book
    paginate_by = 3

    # def get_queryset(self):
    #     """
    #     Get all the `Book` objects from the database.

    #     This method is not really needed since the default `get_queryset` method will return all books. We're keeping it here for demonstration purposes and a reminder that we could override the default behavior.
    #     """
    #     return Book.objects.all()

    def get_context_data(self, **kwargs):
        """
        Get the context data from the `super` class and add some additional context variable to it.
        """
        # `context` will have both `object_list` and `book_list`, by default, from `super`.
        context = super().get_context_data(**kwargs)
        context['additonal_context_variable'] = 'A sample string here(?)'
        return context


class BookDetailView(DetailView):
    model = Book