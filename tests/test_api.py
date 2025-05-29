import unittest
import json
from app.api.main import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        # Flask provides a built-in test client
        self.client = app.test_client()

    # ---------- /predict -----------
    def test_predict_endpoint_json(self):
        resp = self.client.post(
            '/predict',
            json={'message': 'Win a $1000 gift card now!'}
        )
        print(resp.data)
        self.assertEqual(resp.status_code, 200)
        payload = json.loads(resp.data)
        self.assertIn('prediction', payload)

    def test_predict_endpoint_form(self):
        resp = self.client.post(
            '/predict',
            data={'message': 'Hi, shall we meet tomorrow?'},
            content_type='application/x-www-form-urlencoded'
        )
        print(resp.data)
        self.assertEqual(resp.status_code, 200)
        # form version returns rendered HTML, just check for keyword
        self.assertIn(b'Prediction', resp.data)

    # ---------- /train -------------
    def test_train_endpoint(self):
        resp = self.client.post('/train')
        self.assertEqual(resp.status_code, 200)
        payload = json.loads(resp.data)
        self.assertEqual(
            payload.get('message'),
            'Model retrained and saved successfully'
        )

    # ---------- / (home) -----------
    def test_home_page(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'Spam Message Classifier', resp.data)

if __name__ == '__main__':
    unittest.main()
