from django.contrib import admin

from djangoDis.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Product, ProductAdmin)
