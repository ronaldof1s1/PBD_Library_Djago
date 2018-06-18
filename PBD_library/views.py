from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

def index(request):
    return render(request, 'PBD_library/index.html')

def books_list(request):
    books = Book.objects.all()

    return render(request, 'PBD_library/books_list.html', {'books': books})

def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    authors = book.authors.all()
    copies = book.copies.all()

    return render(request, 'PBD_library/book_detail.html', {'book':book, 'authors':authors, 'copies':copies})

def users_list(request):
    users = User.objects.all()

    return render(request, 'PBD_library/users_list.html', {'users':users})

def user_detail(request, user_id):
    user = User.objects.get(pk=user_id)
    loans = user.loans.all()
    copies = []
    for loan in loans:
        copies.append(loan.copy)

    return render(request, 'PBD_library/user_detail.html', {'user': user, 'loans': loans, 'copies': copies})
