from django.contrib import admin
from webapp.models import Category
from webapp.models import Product


class ProductAdmin(admin.ModelAdmin):
    # list_display = ['id', 'name', 'description', 'category', 'balance', 'price']
    # list_filter = ['category']
    search_fields = ['name', 'category', 'price']
    fields = ['name', 'description', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    # list_display = ['*']
    # list_filter = ['*']
    search_fields = ['*']
    fields = ['name', 'description']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
