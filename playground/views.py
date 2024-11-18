from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
# Create your views here.

def say_hello(request):
    products = Product.objects.all()
    for i in products:
        print(i)
    return render(request, 'index.html', {'name':'Vijayaraj Pushpalingam'})
