from django.contrib import admin

from .models import Client, Supplier, Category, Product, Delivery, DeliveryItem, Sale, SaleItem

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact')
    search_fields = ('name',)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'payment_method')
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'category', 'value')
    search_fields = ('name',)


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('creation_date', )
    search_fields = ('creation_date',)


@admin.register(DeliveryItem)
class DeliveryItemAdmin(admin.ModelAdmin):
    list_display = ('delivery', 'item', 'sell_value', 'percentage')
    search_fields = ('delivery',)


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('creation_date', )
    search_fields = ('creation_date',)


@admin.register(SaleItem)
class SaleItemAdmin(admin.ModelAdmin):
    list_display = ('sale', 'value', 'expense', 'expense_description')
    search_fields = ('sale',)
