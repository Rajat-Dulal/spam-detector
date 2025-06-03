import json
from app import app

def test_spam_prediction():
    client = app.test_client()
    response = client.post('/predict', json={'text': 'Win money now!'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'prediction' in data
    assert data['prediction'] in ['spam', 'not spam']
