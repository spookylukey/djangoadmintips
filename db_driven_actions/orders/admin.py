from django.contrib import admin

from .models import Customer, Order, OrderItem, Product


class OrderItemInline(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    model = Order
    list_display = ['id', 'customer', 'total', 'timestamp']


admin.site.register(Customer)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product)
