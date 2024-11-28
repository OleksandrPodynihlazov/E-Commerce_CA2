from django.contrib import admin
from .models import Category, Product, ControlMechanism

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category, CategoryAdmin)

class ControlMechanismAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(ControlMechanism, ControlMechanismAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'category', 'control_mechanism', 'stock', 'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    list_per_page = 20

admin.site.register(Product, ProductAdmin)