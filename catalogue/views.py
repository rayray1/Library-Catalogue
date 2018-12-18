from django.shortcuts import render
from catalogue.models import Book, Author, BookInstance, Genre
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # Authors
    num_authors = Author.objects.count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render HTML template
    return render(request, 'index.html', context=context)

# Book list
class BookListView(generic.ListView):
    model = Book
    paginate_by = 10

# Book detail
class BookDetailView(generic.DetailView):
    model = Book

# Author list
class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

# Author detail
class AuthorDetailView(generic.DetailView):
    model = Author

# Loaned out books
class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'catalogue/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
