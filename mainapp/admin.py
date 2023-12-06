from django.contrib import admin
from .models import Product, Category, Order, ProductAdd


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'is_active']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['is_active',]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','quantity', 'category', 'price',]
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['name','category']
    list_editable = ['price','quantity']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user_profile','total_price',  'quantity', 'taken']
    list_filter = ['product','user_profile']
    list_editable = ['taken',]

@admin.register(ProductAdd)
class ProductAddAdmin(admin.ModelAdmin):
    list_display = ['product_add',  'quantity_add']
    
