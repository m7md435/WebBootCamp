from django.shortcuts import render
from django.http import Http404

# In-memory books list
BOOKS = [
    {
        'id': 1,
        'title': 'The Django Book',
        'author': 'Adrian Holovaty',
        'description': 'A comprehensive guide to building web applications with Django.',
        'year': 2009
    },
    {
        'id': 2,
        'title': 'Python Crash Course',
        'author': 'Eric Matthes',
        'description': 'Learn Python programming through hands-on projects.',
        'year': 2019
    },
    {
        'id': 3,
        'title': 'Two Scoops of Django',
        'author': 'Daniel Audicino',
        'description': 'Best practices and patterns for Django development.',
        'year': 2017
    },
    {
        'id': 4,
        'title': 'Clean Code',
        'author': 'Robert C. Martin',
        'description': 'A handbook of agile software craftsmanship.',
        'year': 2008
    },
]

def book_list(request):
    """Display all books"""
    context = {
        'books': BOOKS,
    }
    return render(request, 'library/book_list.html', context)

def book_detail(request, id):
    """Display a single book's details"""
    book = None
    for b in BOOKS:
        if b['id'] == id:
            book = b
            break
    
    if book is None:
        raise Http404("Book not found")
    
    context = {
        'book': book,
    }
    return render(request, 'library/book_detail.html', context)
