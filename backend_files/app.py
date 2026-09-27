from flask import Flask, request, jsonify
import pandas as pd
import joblib

superkart_api = Flask(__name__)
model = joblib.load('superkart_model.joblib')
FEATURES = ['Product_Weight','Product_Sugar_Content','Product_Allocated_Area','Product_MRP','Store_Size','Store_Location_City_Type','Store_Type','Product_Id_char','Store_Age_Years','Product_Type_Category']

@superkart_api.get('/health')
def health():
    return jsonify({'status':'ok'})

@superkart_api.post('/v1/predict')
def predict():
    payload = request.get_json(force=True)
    frame = pd.DataFrame([payload])[FEATURES]
    pred = float(model.predict(frame)[0])
    return jsonify({'predicted_sales': pred})

@superkart_api.post('/v1/predictbatch')
def predict_batch():
    frame = pd.read_csv(request.files['file'])[FEATURES]
    preds = model.predict(frame)
    return jsonify({str(i): float(v) for i, v in enumerate(preds)})

if __name__ == '__main__':
    superkart_api.run(host='0.0.0.0', port=7860)
