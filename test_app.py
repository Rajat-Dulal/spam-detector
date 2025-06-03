import json
from app import app

def test_prediction():
    client = app.test_client()
    response = client.post('/predict', json={'text': 'Congratulations! You won a prize!'})
    assert response.status_code == 200
    assert 'prediction' in response.get_json()
