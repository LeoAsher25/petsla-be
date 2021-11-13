from django.contrib import admin
from django.db import models
from store.models import * 

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price', 'stock', 'category', 'modified_date',)
    list_filter = ('category', 'modified_date')
    search_fields = ('product_name', 'category')
    actions_on_top = False
    list_per_page = 20

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price',)
    search_fields = ('product',)
    actions_on_top = False
    list_per_page = 20

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user','number_phone', 'total_price', 'created_at', 'is_delivered', 'is_paid')   
    search_fields = ('user', 'number_phone',)
    list_filter = ('created_at', 'is_paid', 'is_delivered',)
    list_per_page = 20
    # actions_on_top = False
    actions_selection_counter = False

class CategoryAdmin(admin.ModelAdmin): 
    search_fields = ('category_name',)
    list_display = ('id', 'category_name', 'created_at')
    list_filter = ('created_at',)
    actions_on_top = False
    actions_selection_counter = False


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Category, CategoryAdmin)


 