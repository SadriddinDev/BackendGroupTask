from django.contrib import admin
from main.models import Deliver, Product, ProductItem, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Deliver)
class DeliverAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']


@admin.register(ProductItem)
class ProductItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'deliver', 'price', 'quantity', 'base_price']
