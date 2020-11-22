from django.contrib import admin

from djangoDis.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'item_condition_id', 'category_name', 'brand_name', 'price', 'shipping',
                    'item_description']


admin.site.register(Product, ProductAdmin)
