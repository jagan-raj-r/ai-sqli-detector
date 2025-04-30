import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import os

# Load the dataset
df = pd.read_csv('data/payload_dataset.csv')

# Remove rows with NaN values in 'payload' column
df = df.dropna(subset=['payload'])

# Prepare features and labels
X = df['payload']
y = df['label']

# Convert text data to feature vectors using CountVectorizer
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# Train the classifier (Logistic Regression)
classifier = LogisticRegression()
classifier.fit(X_train, y_train)

# Evaluate the model
y_pred = classifier.predict(X_test)
print(classification_report(y_test, y_pred))

# Ensure the 'models' directory exists
os.makedirs('models', exist_ok=True)

# Save the trained model and vectorizer
joblib.dump(classifier, 'models/sql_injection_detector.pkl')
joblib.dump(vectorizer, 'models/vectorizer.pkl')
