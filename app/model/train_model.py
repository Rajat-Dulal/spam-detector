import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

def train_and_save_model():
    data = pd.read_csv(
        'https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv',
        sep='\t', header=None, names=['label', 'message']
    )
    data['label_num'] = data.label.map({'ham': 0, 'spam': 1})

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(data['message'])
    y = data['label_num']

    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2)

    model = MultinomialNB()
    model.fit(X_train, y_train)

    with open('app/model/model.pkl', 'wb') as f:
        pickle.dump((model, vectorizer), f)

    print("✅ Model and vectorizer saved to 'model.pkl'")
