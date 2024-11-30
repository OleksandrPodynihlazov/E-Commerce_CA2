from shop.models import Product, Category, Brand
from django.views.generic import ListView
from django.db.models import Q
from django.shortcuts import render


# class SearchResultsListView(ListView):
#     model = Product
#     context_object_name = "product_list"
#     template_name = "search.html"

#     def get_queryset(self):
#         query = self.request.GET.get("q")
#         return Product.objects.filter(
#             Q(name__icontains=query) | Q(description__icontains=query)
#         )

#     def get_context_data(self, **kwargs):
#         context = super(SearchResultsListView, self).get_context_data(**kwargs)
#         context["query"] = self.request.GET.get("name")
#         return context
    
def search(request):
    qs = Product.objects.all()

    name_query = request.GET.get('name')
    category_query = request.GET.get('category')
    brand_query = request.GET.get('brand')
    min_price = request.GET.get('minPrice')
    max_price = request.GET.get('maxPrice')

    lower_price = qs.order_by('price').first().price
    upper_price = qs.order_by('-price').first().price

    if name_query != '' and name_query is not None:
        qs = qs.filter(name__icontains=name_query)
    
    if category_query != '' and category_query is not None and category_query != 'Show All':
        qs = qs.filter(category__name__icontains=category_query)
    
    if brand_query != '' and brand_query is not None and brand_query != 'Show All':
        qs = qs.filter(brand__name__icontains=brand_query)
    
    if min_price != '' and min_price is not None:
        qs = qs.filter(price__gte=min_price)
    
    if max_price != '' and max_price is not None:
        qs = qs.filter(price__lt=max_price)

    context = {
        'queryset': qs,
        'categories': Category.objects.all(),
        'brands': Brand.objects.all,
        'lower_price': lower_price,
        'upper_price': upper_price
    }
    return render(request, 'search.html', context)
