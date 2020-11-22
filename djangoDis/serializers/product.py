from rest_framework import serializers

from djangoDis.models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['id',
                  'name',
                  'item_condition_id',
                  'category_name',
                  'brand_name',
                  'price',
                  'shipping',
                  'item_description',
                  ]
