from django.contrib import admin
from .models import CategoryModel, ProductModel, CartModel

# Register your models here.

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_title', 'created_at']
    search_fields = ['category_title']
    list_filter = ['created_at']

@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_title', 'product_count', 'product_price', 'product_created_at']
    search_fields = ['product_title', 'product_category']
    list_filter = ['product_created_at']
    save_as = True
    save_on_top = True

@admin.register(CartModel)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'user_add_date']
    search_fields = ['user_id']
    list_filter = ['user_add_date']
