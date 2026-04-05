from django.shortcuts import render
from .models import Book

# Create your views here.
#
def index(request):
    oldest_books = Book.objects.order_by("publish_date")[:10]
    return render(request,'lab1django/index.html',{"oldest_books":oldest_books})
