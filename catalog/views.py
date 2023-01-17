import datetime

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView

from catalog.forms import RenewBookForm
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

    # Get number of visits `num_visits` from the session object. If it doesn't exist, set it to 0.
    num_visits = request.session.get('num_visits', 0)
    # Increment `num_visits` by 1 and then save that new value to `num_visits` in the session object.
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
    paginate_by = 4

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


class AuthorListView(ListView):
    model = Author
    paginate_by = 3


class AuthorDetailView(DetailView):
    model = Author
    
class LoanedBooksByUserListView(LoginRequiredMixin, ListView):
    """
    Generic class-based view listing books on loan to current user.
    """
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 5

    def get_queryset(self):
        return BookInstance.objects.filter(
            borrower=self.request.user
        ).filter(
            status__exact='o'
        ).order_by('due_back')


class LoanedBooksAllListView(PermissionRequiredMixin, ListView):
    """
    Generic class-based view listing all books on loan.
    """
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_all.html'
    paginate_by = 10
    permission_required = 'catalog.can_mark_returned'

    def get_queryset(self):
        return BookInstance.objects.filter(
            status__exact='o'
        ).order_by('due_back')



@login_required
@permission_required('catalog.can_mark_returned', raise_exception=True)
def renew_book_librarian(request, pk):
    book_instance = get_object_or_404(BookInstance, pk=pk)

    if request.method == 'POST':

        form = RenewBookForm(request.POST)

        if form.is_valid():
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()

            return HttpResponseRedirect(reverse('catalog:all-borrowed'))

    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'catalog/book_renew_librarian.html', context)
