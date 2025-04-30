from flask import Flask, request, render_template_string, jsonify
import joblib
import os

app = Flask(__name__)

# Load model and vectorizer
MODEL_PATH = 'models/sql_injection_detector.pkl'
VECTORIZER_PATH = 'models/vectorizer.pkl'

if not os.path.exists(MODEL_PATH) or not os.path.exists(VECTORIZER_PATH):
    raise FileNotFoundError("Model or vectorizer file missing. Train the model first.")

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

# Styled HTML template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>AI SQL Injection Detector</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f6f8;
            padding: 40px;
            color: #333;
        }
        .container {
            max-width: 700px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        h2 {
            text-align: center;
            color: #2c3e50;
        }
        label, input[type="text"] {
            display: block;
            width: 100%;
            margin-bottom: 15px;
            font-size: 16px;
        }
        input[type="text"] {
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 6px;
        }
        input[type="submit"] {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 12px 20px;
            font-size: 16px;
            border-radius: 6px;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #2980b9;
        }
        .result {
            margin-top: 20px;
            padding: 10px;
            border-radius: 6px;
        }
        .safe {
            background-color: #eafaf1;
            color: #2d8a4b;
        }
        .malicious {
            background-color: #fdecea;
            color: #c0392b;
        }
        .error {
            background-color: #fff3cd;
            color: #856404;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>AI-Based SQL Injection Detector</h2>
        <form method="post">
            <label for="query">Enter SQL Query or Input:</label>
            <input type="text" name="query" id="query" value="{{ query or '' }}" required>
            <input type="submit" value="Check">
        </form>

        {% if prediction is not none %}
            <div class="result {{ 'malicious' if prediction == 1 else 'safe' }}">
                <strong>Prediction:</strong> {{ 'Malicious' if prediction == 1 else 'Safe' }}
            </div>
        {% elif error %}
            <div class="result error">
                <strong>Error:</strong> {{ error }}
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    error = None
    query = None

    if request.method == 'POST':
        query = request.form.get('query')
        if query:
            try:
                vector = vectorizer.transform([query])
                prediction = model.predict(vector)[0]
            except Exception as e:
                error = str(e)
        else:
            error = "Query cannot be empty."

    return render_template_string(HTML_TEMPLATE, prediction=prediction, error=error, query=query)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data or 'query' not in data:
        return jsonify({'error': 'No query provided'}), 400
    try:
        query = data['query']
        vector = vectorizer.transform([query])
        prediction = model.predict(vector)[0]
        return jsonify({'prediction': int(prediction)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
