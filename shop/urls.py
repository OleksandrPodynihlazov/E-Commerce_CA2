from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.cat_list, name='cat_list'),
    # path('category/<uuid:cat>/', views.product_detail, name='product_detail'),
    path('<str:category_name>/', views.prod_list, name = 'products_by_category'),
    # path('<uuid:category_id>/<uuid:product_id>/', views.product_detail, name = 'product_detail'),
]
