from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status', 'collection_title']
    list_editable = ['unit_price']
    list_select_related = ['collection'] # qs.select_related for admin
    
    @admin.display(ordering='inventory') # For applying Ordering on Computed Field
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'LOW'
        return 'OK'
    
    def collection_title(self, product):
        return product.collection.title


admin.site.register(models.Collection)

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 50
    
@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at', 'customer']