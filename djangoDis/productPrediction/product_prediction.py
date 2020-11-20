from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from djangoDis.models import Product




@api_view(['DELETE'])
def delete_all_products(request):
    Product.objects.all().delete()
    return Response(status=status.HTTP_200_OK)