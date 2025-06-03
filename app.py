from flask import Flask, request, jsonify, render_template
import joblib
import logging

# Set up logging to a file
logging.basicConfig(filename='app.log', level=logging.INFO)

app = Flask(__name__)
model = joblib.load('spam_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get input from HTML form field named "email"
        text = request.form.get('email', '')
        prediction = model.predict([text])[0]
        result = 'spam' if prediction == 1 else 'not spam'
        logging.info(f"[form] '{text}' → {result}")
        return render_template('index.html', prediction=result.upper())
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_api():
    if request.is_json:
        data = request.get_json()
        text = data.get('text', '')
        prediction = model.predict([text])[0]
        result = 'spam' if prediction == 1 else 'not spam'
        logging.info(f"[json] '{text}' → {result}")
        return jsonify({'prediction': result})
    return jsonify({'error': 'Invalid content type'}), 415

@app.route('/health')
def health():
    return jsonify({'status': 'ok'}), 200

@app.route('/metrics')
def metrics():
    return jsonify({
        'uptime_hours': 72,
        'total_predictions': 1234,
        'status': 'running'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
