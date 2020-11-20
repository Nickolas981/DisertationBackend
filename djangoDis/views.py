from django.http import JsonResponse
from django_rest.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from djangoDis.models import Product


def homePage(request):
    Product(name="тест товару").save()
    data = list(Product.objects.values())
    return JsonResponse(data, safe=False)

