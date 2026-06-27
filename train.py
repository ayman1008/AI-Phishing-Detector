import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# 1. Data load karna

df = pd.read_csv('phishing_emails.csv')

# 2. Vectorizer setup

vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X = vectorizer.fit_transform(df['text'])
y = df['label']

# 3. Model training

model = LogisticRegression()
model.fit(X, y)

# 4. Files save karna

joblib.dump(model, 'model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

print("Model successfully train ho gaya aur save ho gaya!")