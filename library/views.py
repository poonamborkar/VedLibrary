from django.shortcuts import render

from .models import Books
# Create your views here.

def home(request):
    books = Books.objects.all()
    return render(request, 'libraryhome.html',{'books': books})

def signup(request):
    return render(request, 'signup.html')
