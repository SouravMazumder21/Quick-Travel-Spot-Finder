from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained ML model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to Quick Travel Spot Finder API!"})

# API Endpoint for Prediction
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Get JSON input
    temperature = data['temperature']
    popularity = data['popularity']

    # Prepare input for model
    features = np.array([[temperature, popularity]])

    # Make prediction
    prediction = model.predict(features)[0]

    return jsonify({'recommended': bool(prediction)})

if __name__ == '__main__':
    app.run(debug=True)

