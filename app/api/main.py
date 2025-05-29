from flask import Flask, request, jsonify, render_template
from app.api.utils import predict_spam
from app.model.train_model import train_and_save_model
import logging
import os

app = Flask(__name__, template_folder='../templates')

# Setup logging
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/prediction.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

@app.route('/')
def home():
    return render_template("form.html")

@app.route('/predict', methods=['POST'])
def predict():
    message = request.json.get('message') if request.is_json else request.form.get('message')
    if not message:
        return jsonify({'error': 'No message provided'}), 400

    prediction = predict_spam(message)
    result = 'spam' if prediction else 'not spam'

    logging.info(f"Prediction: {result} | Message: {message}")

    if request.is_json:
        return jsonify({'prediction': result})
    else:
        return render_template("form.html", prediction=result, message=message)

@app.route('/train', methods=['POST'])
def retrain():
    train_and_save_model()
    return jsonify({'message': 'Model retrained and saved successfully'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
