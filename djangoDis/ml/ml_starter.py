import joblib
import pandas as pd
import numpy as np

from djangoDis.ml.backend.encoders import get_encodings
from djangoDis.ml.backend.models import f_regr
from djangoDis.ml.backend.preprocessing import preprocess

scaler = joblib.load('./backend/assets/files/scaler.pickle')

model = f_regr()
model.load_weights('./backend/assets/models/model.h5')

columns = ['name', 'item_condition_id', 'brand_name', 'category_name', 'shipping', 'item_description']

def predict():
    features = ['Iphone X 256', '5', 'apple', '', '1', 'test']

    data = np.array(features)

    df = pd.DataFrame([data], columns=columns)

    processed_data = preprocess(df)

    encoded_data = get_encodings(processed_data)

    pred = model.predict(encoded_data)
    prediction = np.expm1(scaler.inverse_transform(pred.reshape(-1, 1))[:,0])

    print(prediction[0])