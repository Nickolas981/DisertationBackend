import joblib
import pandas as pd
import numpy as np

from djangoDis.ml.backend.encoders import get_encodings
from djangoDis.ml.backend.models import f_regr
from djangoDis.ml.backend.preprocessing import preprocess

from rest_framework.decorators import api_view
from djangoDis.serializers.product import ProductSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status

scaler = joblib.load('djangoDis/ml/backend/assets/files/scaler.pickle')

model = f_regr()
model.load_weights('djangoDis/ml/backend/assets/models/model.h5')

columns = ['name', 'item_condition_id', 'brand_name', 'category_name', 'shipping', 'item_description']


def predict(name):
    features = [name, '5', 'apple', '', '1', 'test']

    data = np.array(features)

    df = pd.DataFrame([data], columns=columns)

    processed_data = preprocess(df)

    encoded_data = get_encodings(processed_data)

    pred = model.predict(encoded_data)
    prediction = np.expm1(scaler.inverse_transform(pred.reshape(-1, 1))[:,0])

    return prediction[0]


@api_view(['POST'])
def predict_price(request):
    serializer = ProductSerializer(data=request.data)
    if (serializer.is_valid()):
        return JsonResponse({
            "price": predict(request.data['name'])
        })
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)