import pickle

def load_model():
    with open('app/model/model.pkl', 'rb') as f:
        model, vectorizer = pickle.load(f)
    return model, vectorizer

def predict_spam(message):
    model, vectorizer = load_model()
    try:
        X = vectorizer.transform([message])
        return model.predict(X)[0]
    except Exception as e:
        print("Prediction error:", e)
        raise