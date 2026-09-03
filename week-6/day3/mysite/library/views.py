from django.shortcuts import render
from django.http import Http404

# In-memory books list
BOOKS = [
    {
        'id': 1,
        'title': 'Journey to Baghdad',
        'author': 'Mohammad Hassan',
        'description': 'A beautiful story about traveling through ancient Baghdad.',
        'year': 2015
    },
    {
        'id': 2,
        'title': 'Tales of the Desert',
        'author': 'Fatima Aisha',
        'description': 'Exciting adventures and mysteries in the desert.',
        'year': 2018
    },
    {
        'id': 3,
        'title': 'Wisdom of the Ancients',
        'author': 'Ahmed Omar',
        'description': 'Ancient Arabic wisdom and philosophy lessons.',
        'year': 2012
    },
    {
        'id': 4,
        'title': 'The House of Roses',
        'author': 'Layla Noor',
        'description': 'A romantic tale of love and family traditions.',
        'year': 2020
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
