from django.shortcuts import render, get_object_or_404
from.models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage

def prod_list(request, category_name=None):
    category = None
    products = Product.objects.filter(available=True)

    if category_name:
        category = get_object_or_404(Category, slug=category_name)
        products = Product.objects.filter(category=category, available=True)

    paginator = Paginator(products, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except(EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)
    
    return render(request, 'shop/category.html', {'category':category, 'prods':products})
    

def cat_list(request):
    categories = Category.objects.all()
    categories = sorted(categories, key=lambda x: len(x.name))
    return render(request, 'shop/categories.html', {'category':categories})

def product_detail(request, category_name, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/product.html', {'product':product})
