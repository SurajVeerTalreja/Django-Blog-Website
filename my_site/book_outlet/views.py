from django.shortcuts import render
from .models import Book
from django.db.models import Avg

# Create your views here.
def index(request):
    all_books = Book.objects.all().order_by('-rating')
    total_num_of_books = all_books.count()
    avg_rating = all_books.aggregate(Avg('rating'))

    context = {
        'books': all_books,
        'total_num_of_books': total_num_of_books,
        'avg_rating': avg_rating,
    }
    return render(request, 'book_outlet/index.html', context=context)


def book_detail(request, slug):
    selected_book = Book.objects.get(slug=slug)

    context = {
        'title': selected_book.title,
        'author': selected_book.author,
        'rating': selected_book.rating,
        'is_bestselling': selected_book.is_bestselling,
    }
    return render(request, 'book_outlet/book-detail.html', context=context)