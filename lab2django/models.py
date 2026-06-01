from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime(2005, 1, 17))

    def __str__(self):
        return f"Customer {self.name} {self.surname}"


class Product(models.Model):
    created_at = models.DateTimeField(default=datetime(2005, 1, 17))
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Product {self.name} {self.price}"


class Cart(models.Model):
    created_at = models.DateTimeField(default=datetime(2005, 1, 17))
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
    )
    products = models.ManyToManyField(Product, through="ProductInCart")
    is_active = models.BooleanField(default=False)

    @property
    def total_price(self):
        total = 0
        for item in ProductInCart.objects.filter(cart=self).select_related("product"):
            total += item.product.price * item.quantity
        return total

    @property
    def total_quantity(self):
        total = 0
        for item in ProductInCart.objects.filter(cart=self).select_related("product"):
            total += item.quantity
        return total

    def __str__(self):
        return f"Cart id:{self.pk} with customer:{self.customer}"


class ProductInCart(models.Model):
    created_at = models.DateTimeField(default=datetime(2005, 1, 17))
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(1000)]
    )

    def __str__(self):
        return f"{self.product.name} in count {self.quantity} in cart id:{self.cart.pk}"
