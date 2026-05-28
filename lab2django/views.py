from django.shortcuts import render
from .models import Cart

# Create your views here.
def carts(request):
    carts  = Cart.objects.order_by("created_at")
    return render(request,"lab2django/carts.html",{"carts":carts})
