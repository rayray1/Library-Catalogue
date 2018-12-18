from django.shortcuts import render
from catalogue.models import Book, Author, BookInstance, Genre
from django.views import generic


def index(request):

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # Authors
    num_authors = Author.objects.count()

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
