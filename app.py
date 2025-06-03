from flask import Flask, request, jsonify
import joblib
import logging

# Set up logging
logging.basicConfig(filename='app.log', level=logging.INFO)

app = Flask(__name__)
model = joblib.load('spam_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get('text', '')
    prediction = model.predict([text])[0]
    result = 'spam' if prediction == 1 else 'not spam'
    logging.info(f"Prediction made: '{text}' → {result}")
    return jsonify({'prediction': result})

@app.route('/')
def home():
    return '''
        <h1>Spam Detector</h1>
        <form method="POST" action="/predict">
            <input name="text" placeholder="Enter message" />
            <input type="submit" />
        </form>
    '''

@app.route('/health')
def health():
    return jsonify({'status': 'ok'}), 200

@app.route('/metrics')
def metrics():
    return jsonify({
        'uptime_hours': 72,
        'total_predictions': 1234,  # (You can make this dynamic later)
        'status': 'running'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
