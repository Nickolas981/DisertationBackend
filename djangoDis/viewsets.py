
from rest_framework import viewsets
from rest_framework import permissions

from djangoDis.models import Product
from djangoDis.serializers.product import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
