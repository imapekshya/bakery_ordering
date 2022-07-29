from django.contrib import admin
from .models import *
# Register your models here.


# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'branch', 'selling_price',
#                     'description', 'stock', 'weight', 'category', 'product_image')


# class CartAdmin(Cart.ModelAdmin):
#     list_display = ('user', 'product', 'quantity')


admin.site.register(Branch)
# admin.site.register(Product, ProductAdmin)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Payment)
admin.site.register(Cart)
# admin.site.register(Cart, CartAdmin)
admin.site.register(OrderPlaced)
