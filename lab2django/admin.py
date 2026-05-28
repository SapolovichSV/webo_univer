from django.contrib import admin

from .models import Cart,Product,ProductInCart,Customer
class ProductInCartInline(admin.TabularInline):
    model = ProductInCart

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [ProductInCartInline]
    list_display = ("id","customer","created_at")
    search_fields = (
        "customer__name",
        "customer__surname",
    )
    list_filter = (
        "created_at",
        "customer",
    )

admin.site.register(Product)
admin.site.register(Customer)

# Register your models here.
