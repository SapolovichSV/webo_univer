from django.utils.html import format_html
from django.contrib import admin

from .models import Cart, Product, ProductInCart, Customer


class ProductInCartInline(admin.TabularInline):
    model = ProductInCart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [ProductInCartInline]
    list_display = ("id", "customer", "created_at", "total_price", "total_quantity","is_active")
    search_fields = (
        "customer__name",
        "customer__surname",
    )
    list_filter = (
        "created_at",
        "customer",
    )
    readonly_fields = ("total_price","total_quantity")
    fieldsets = (("Total info", {"fields": ("total_price", "total_quantity")},),("Main Info",{"fields":("customer","is_active")}))
    date_hierarchy = "created_at"
    @admin.display(description="Status")
    def active_status(self, obj):
        if obj.is_active:
            return format_html(
                '<span style="color: green; font-weight: bold;">Active</span>'
            )

        return format_html(
            '<span style="color: red; font-weight: bold;">Inactive</span>'
        )


admin.site.register(Product)
admin.site.register(Customer)

# Register your models here.
