from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F, Value, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.db.models.aggregates import Avg,Max,Min,Count
from django.contrib.contenttypes.models import ContentType
from django.db import transaction
from store.models import Product,OrderItem,Customer,Order, Collection, Promotion
from tags.models import TaggedItem

# Create your views here.

def say_hello(request):
    # query_set = Product.objects.filter(inventory__lt=10,unit_price__lt = 10)
    # query_set = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))
    # query_set = Product.objects.filter(inventory=F('collection_id'))
    # query_set = Product.objects.all().order_by('-title')
    # query_set = Product.objects.values('id','title','collection__title')
    # values = OrderItem.objects.values('product_id').distinct()
    # query_set = Product.objects.filter(id__in = values)
    # orders = Order.objects.select_related('customer').order_by('-placed_at')[:5]
    # items = OrderItem.objects.filter(order_id__in = (orders)).select_related("product")
    # result = Product.objects.aggregate(count = Count('id'),mini_price = Min('unit_price'),max_price = Max('unit_price'))
    # add = Product.objects.annotate(new_id = Value(True),full_name = Concat('title',Value(" "),'title'))
    # content_type = ContentType.objects.get_for_model(Product)
    # query_set = TaggedItem.objects.select_related('tag').filter(content_type = content_type,object_id = 1)
    # with transaction.atomic():
    #     order = Order()
    #     order.customer_id = 5
    #     order.save()
        
    #     item = OrderItem()
    #     item.order_id = order.id
    #     item.product_id = 1
    #     item.quantity = 9
    #     item.unit_price = 398
    #     item.save()
    
    # products = Product.objects.select_related('collection').filter(collection_id = 6).order_by('id')
    # for i in products:
    #     print(i.title,i.unit_price,i.collection.title)
    
    # products = Product.objects.prefetch_related('promotions').filter(promotions__isnull=False)
    # for i in products:
    #     print(i.title)
    #     for j in i.promotions.all():
    #         print(j.description)
    
    # customer = Customer.objects.create(first_name='Suriaya',last_name ='Pushpalingam',email="Suriya@gmai.com",phone='738493')
    # print(customer.id)
    
    # products = Product.objects.select_related('collection').filter(collection__title = 'Beauty')
    # products.update(unit_price = ExpressionWrapper(F('unit_price')*0.9,output_field=DecimalField))
    
    
    # customer = Customer.objects.select_related('order')
    # for i in customer:
    #     print(i.email,i.order.placed_at,i.order.payment_status)
        
    # orders = Order.objects.select_related('customer')
    # for order in orders:
    #     print(order.customer.email, order.payment_status, order.placed_at)
    
    collections_max_price = Collection.objects.annotate(max_price = Max('product__unit_price'))
    print(list(collections_max_price))
    for collection in collections_max_price:
        products = Product.objects.filter(collection = collection, unit_price = collection.max_price)
        for product in products:
            print(product.title, product.unit_price,product.collection.title)
            
    collections = Product.objects.values('collection_id').distinct()
    print(list(collections))
    return render(request, 'index.html', {'name':'Vijayaraj Pushpalingam'})


 