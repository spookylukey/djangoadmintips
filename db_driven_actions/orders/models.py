from enum import Enum

from django.conf import settings
from django.db import models
from enumfields import EnumField


class Customer(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='orders')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0}: {1} - {2}".format(self.id, self.customer, self.timestamp)

    class Meta:
        ordering = ['timestamp']

    @property
    def total(self):
        return sum(line.total for line in self.items.all())


class OrderItem(models.Model):
    product = models.ForeignKey(Product, related_name='orders')
    quantity = models.PositiveIntegerField()
    order = models.ForeignKey(Order, related_name='items')

    def __str__(self):
        return "{0} x {1}".format(self.product, self.quantity)

    @property
    def total(self):
        return self.quantity * self.product.price


class ActionType(Enum):
    assigned = 'A'
    picked = 'P'
    shipped = 'S'


class OrderAction(models.Model):
    order = models.ForeignKey(Order, related_name='actions')
    action = EnumField(ActionType, max_length=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0}, user {1}".format(self.action.name, self.user)
