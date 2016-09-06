from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib import messages

from .models import Customer, Order, OrderItem, Product


class OrderItemInline(admin.TabularInline):
    model = OrderItem


# We need a unique callable for each action:
def make_assign_to_user_action(user):
    def assign_to_user(modeladmin, request, queryset):
        for order in queryset:
            order.assign_to(user)
            messages.info(request, "Order {0} assigned to {1}".format(order.id,
                                                                      user.first_name))

    assign_to_user.short_description = "Assign to {0}".format(user.first_name)
    # We need a different '__name__' for each action - Django
    # uses this as a key in the drop-down box.
    assign_to_user.__name__ = 'assign_to_user_{0}'.format(user.id)

    return assign_to_user


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    model = Order
    list_display = ['id', 'customer', 'total', 'timestamp']

    def get_actions(self, request):
        actions = super(OrderAdmin, self).get_actions(request)

        for user in get_user_model().objects.filter(is_staff=True).order_by('first_name'):
            action = make_assign_to_user_action(user)
            actions[action.__name__] = (action,
                                        action.__name__,
                                        action.short_description)

        return actions

admin.site.register(Customer)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product)
