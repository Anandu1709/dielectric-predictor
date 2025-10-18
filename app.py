from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open("dielectric_model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    infill_density = float(data['infill_density'])
    infill_pattern = int(data['infill_pattern'])
    printing_speed = float(data['printing_speed'])

    # Prepare input for prediction
    input_features = np.array([[infill_density, infill_pattern, printing_speed]])
    prediction = model.predict(input_features)[0]

    result = {
        'dielectric_constant': round(prediction[0], 4),
        'tan_delta': round(prediction[1], 6),
        'q_factor': round(prediction[2], 4)
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
