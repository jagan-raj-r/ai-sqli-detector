import joblib

# Load the trained model and vectorizer
model = joblib.load('models/sql_injection_detector.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')

# Get input from the user
payload = input("Enter SQL query to check for injection: ")

# Vectorize the input
payload_vectorized = vectorizer.transform([payload])

# Make the prediction
prediction = model.predict(payload_vectorized)

# Output the result
if prediction[0] == 1:
    print("This is a SQL Injection payload!")
else:
    print("This is a safe SQL query.")
