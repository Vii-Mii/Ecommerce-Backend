from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
    
from store.models import Product,OrderItem
# Create your views here.

def say_hello(request):
    # query_set = Product.objects.filter(inventory__lt=10,unit_price__lt = 10)
    # query_set = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    # query_set = Product.objects.filter(inventory=F('collection_id'))
    # query_set = Product.objects.all().order_by('-title')
    # query_set = Product.objects.values('id','title','collection__title')
    values = OrderItem.objects.values('product_id').distinct()
    query_set = Product.objects.filter(id__in = values)
    return render(request, 'index.html', {'name':'Vijayaraj Pushpalingam','products':query_set})


