from flask import Flask, request, jsonify
import numpy as np
import joblib

app = Flask(__name__)

model = joblib.load('iris_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    predict_request = [data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']]
    predict_request = np.array([predict_request])
    prediction = model.predict(predict_request)
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run( host='0.0.0.0',port=5000, debug=True)
