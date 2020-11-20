from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from djangoDis.serializers.product import ProductSerializer


@api_view(['POST'])
def predict_price(request):
    serializer = ProductSerializer(data=request.data)
    if (serializer.is_valid()):
        return JsonResponse({
            "price": "100"
        })
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


