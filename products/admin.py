from django.contrib import admin
from products.models import Category, Product, Manufacturer, Supplier, Unit


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ...

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    ...

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    ...

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    ...
