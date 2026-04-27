from django.contrib import admin
from .models import Category, Product, Cart, CartItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price']
    list_filter = ['category']
    list_editable = ['price']
    fields = ['category', 'name', 'description', 'price', 'image']

admin.site.register(Cart)
admin.site.register(CartItem)

