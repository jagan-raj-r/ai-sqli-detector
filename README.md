
# 🧠 AI-Based SQL Injection Payload Detector

A lightweight Flask web app that uses machine learning to detect potential SQL injection payloads in user input. This tool is designed for security researchers, ethical hackers, and AppSec engineers who want to explore how AI can assist in basic web security use cases.

---

## 📌 Project Overview

This project implements a basic machine learning model trained on a dataset of SQL injection (SQLi) and normal queries. The app takes input from the user, sends it to the model, and returns whether the input is **SQLi** or **safe**. It is built using Python, Flask, and scikit-learn, and is ideal for educational or proof-of-concept use.

---

## 🧰 Tech Stack

- **Frontend**: HTML/CSS (via Flask templates)
- **Backend**: Python, Flask
- **ML**: scikit-learn (Logistic Regression)
- **Deployment**: Localhost / Flask development server

---

## 📁 Folder Structure

```
ai-sqli-detector/
│
├── app.py                     # Main Flask app
├── model/
│   ├── sql_injection_detector.pkl  # Trained ML model
│   └── vectorizer.pkl              # Vectorized data
├── scripts/
│   ├── train_model.py         # Model training script
│   └── app-backend.py         # Shell based interface
├── data/
│   └── payload_dataset.csv            # Raw input data (payloads + labels)
├── README.md
└── requirements.txt
```

---

## ⚙️ Setup & Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ai-sqli-detector.git
   cd ai-sqli-detector
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv       
   venv\Scripts\activate     # For Windows
   # OR
   source venv/bin/activate  # For macOS/Linux
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Train the model**:
   ```bash
   python scripts/train_model.py
   ```

5. **Run the app**:
   ```bash
   python app.py
   ```

6. **Access it in your browser**:
   ```
   http://127.0.0.1:5000/
   ```

---

## 🧪 Example Inputs to Test

| Payload Example                                      | Expected Label |
|------------------------------------------------------|----------------|
| `' OR '1'='1`                                        | 1 (SQLi)       |
| `admin' --`                                          | 1 (SQLi)       |
| `1 UNION SELECT username, password FROM users`       | 1 (SQLi)       |
| `SELECT * FROM products WHERE id = 5`                | 0 (Safe)       |
| `hello`                                              | 0 (Safe)       |

---

## 💡 Use Case

- Showcasing how AI can be used to detect basic attack patterns in user input.
- Useful as a beginner-friendly AppSec + AI integration project.
- Can be extended with larger datasets, more models, or integrated into a CI/CD pipeline.

---

## 🛡️ Disclaimer

This tool is meant for educational purposes only. It does not replace robust security mechanisms like WAFs or proper input sanitization in production applications.

---

## 📄 License

MIT License

---

## 🙌 Maintainer

**R JAGAN RAJ**  
[LinkedIn](https://www.linkedin.com/in/r-jagan-raj/)  
[GitHub](https://github.com/jagan-raj-r)
