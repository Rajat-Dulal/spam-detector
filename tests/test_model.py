import unittest
from app.api.utils import predict_spam

class TestModel(unittest.TestCase):

    def test_predict_spam(self):
        result = predict_spam("Congratulations, you won a free ticket!")
        self.assertEqual(result, 1)

    def test_predict_ham(self):
        result = predict_spam("Hi, are we still meeting at 6?")
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
