import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# Sample training data
data = pd.DataFrame({
    'text': ['Free entry in 2 a wkly comp', 'Hi Bob, how are you?', 'Win $1000 now!', 'Are we still meeting today?'],
    'label': [1, 0, 1, 0]  # 1 = spam, 0 = ham
})

# Create pipeline
model = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])

# Train
model.fit(data['text'], data['label'])

# Save model
joblib.dump(model, 'spam_model.pkl')
