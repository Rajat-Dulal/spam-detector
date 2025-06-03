from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)
model = joblib.load('spam_model.pkl')

@app.route('/predict', methods=['POST'])
def predict_api():
    data = request.get_json()
    text = data.get('text', '')
    prediction = model.predict([text])
    result = 'spam' if prediction[0] == 1 else 'not spam'
    return jsonify({'prediction': result})

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        text = request.form['email']
        result = model.predict([text])[0]
        prediction = 'Spam' if result == 1 else 'Not Spam'
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
