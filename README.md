# 📧 Spam Email Detector (ML + DevOps)

This project uses a machine learning model (Naive Bayes) to classify emails as **spam** or **not spam**. The model is exposed as a REST API using Flask, and the project is containerized with Docker. The CI/CD pipeline is managed using Jenkins.

---

## 🚀 Features

- 📨 `/predict` – Get spam prediction via JSON or HTML form
- 🔁 `/train` – Retrain the model from scratch
- 🌐 `/` – Web UI for form-based interaction
- 📜 Logging – Predictions and messages logged to `logs/prediction.log`

---

## 🧠 Tech Stack

- Python
- Scikit-learn
- Flask
- Docker
- Jenkins
- Unit testing with `unittest`
- Logging with Python's `logging` module

---

## 📦 Getting Started

### 🔧 1. Train the model

```bash
python app/model/train_model.py
```
### ▶️ 2. Run the Flask server
```bash
python app/api/main.py
```
The app will be available at: http://localhost:5000

## 🧪 Endpoints
### /predict (POST)
Accepts JSON or form-data:

```json
{
  "message": "You won $1000!"
}
```

Returns:
```json
{
  "prediction": "spam"
}
```

### /train (POST)
Retrains the model from the original dataset:

```bash
curl -X POST http://localhost:5000/train
```

### / (GET)
Opens a form-based UI to input and classify messages.

## Logs
All predictions are logged to:

```bash
logs/prediction.log
```

## Running Tests

```bash 
python -m unittest discover tests
```
## 🐳 Docker
To build and run the project in a container:

```bash
docker build -t spam-detector .
docker run -p 5000:5000 spam-detector
```