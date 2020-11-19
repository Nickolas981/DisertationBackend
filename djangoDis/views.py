from django.http import HttpResponse, JsonResponse
from django_rest.decorators import api_view
from rest_framework.views import APIView

from djangoDis.models import Product


def homePage(request):
    Product(name="тест товару").save()
    data = list(Product.objects.values())
    return JsonResponse(data, safe=False)

