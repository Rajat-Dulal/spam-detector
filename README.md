# 📨 Spam Email Detector – DevOps Pipeline (SIT753 HD Task)

This project implements a machine learning-based spam email classifier and wraps it in a full CI/CD DevOps pipeline using Jenkins, Docker, SonarQube, Bandit, and Prometheus.

> ✅ Designed for SIT753: High Distinction Task (7.3)

---

## 📚 Project Overview

A simple Flask web app that uses a trained Naive Bayes classifier to detect spam messages. Users can interact with the application through a web form or API, and DevOps tools ensure build, test, security, deployment, and monitoring automation.

---

## 🔧 Technologies Used

| Category        | Stack/Tool                      |
|----------------|----------------------------------|
| Language        | Python 3.9                      |
| Web Framework   | Flask                          |
| ML Model        | scikit-learn (Naive Bayes)     |
| Testing         | pytest                         |
| Code Quality    | SonarQube                      |
| Security Scan   | Bandit                         |
| CI/CD           | Jenkins                        |
| Containerization| Docker, Docker Compose         |
| Monitoring      | Prometheus, curl               |

---

## 🚀 Features

- ✅ Spam classification via web form and JSON API
- ✅ Fully containerized using Docker
- ✅ Jenkins CI/CD with multi-stage pipeline
- ✅ Unit testing + reporting
- ✅ Code analysis with SonarQube
- ✅ Security checks with Bandit
- ✅ Health checks & Prometheus metrics
- ✅ Monitoring built into the pipeline

---

## 🏗️ Pipeline Stages in Jenkins

| Stage                  | Description                                                  |
|------------------------|--------------------------------------------------------------|
| **Build**              | Builds the Docker image for the Flask app                    |
| **Test**               | Runs unit tests with pytest, archives test results           |
| **Code Quality**       | Triggers SonarQube analysis                                  |
| **Security**           | Executes Bandit static code analysis                         |
| **Deploy to Test**     | Deploys app using Docker Compose on port `5000`              |
| **Release to Prod**    | Deploys container to `5050`, simulating production           |
| **Monitoring**         | Jenkins checks health via `/health`, Prometheus scrapes `/metrics` |

---

## 🔗 Running the Project Locally

### 1. Clone the repo

```bash
git clone https://github.com/your-username/spam-detector.git
cd spam-detector
```

### 2. Build and run via Docker Compose

```bash
docker network create jenkins  # Only once
docker compose up -d
```

### 3. Open Services

| Service         | URL                      |
|----------------|---------------------------|
| Jenkins         | http://localhost:8080     |
| SonarQube       | http://localhost:9000     |
| App (Test)      | http://localhost:5000     |
| App (Prod)      | http://localhost:5050     |
| Prometheus      | http://localhost:9090     |
| Health Check    | http://localhost:5050/health |
| Metrics         | http://localhost:5050/metrics |

---

## 💬 Example Usage

### 🌐 Web Form

Go to `http://localhost:5050`, type a message like:

```
"Get FREE money now!"
```

Submit and see prediction: `SPAM`.

### 🔧 API Call

```bash
curl -X POST http://localhost:5050/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello, are we still meeting today?"}'
```

Returns:
```json
{"prediction": "not spam"}
```

---

## 📈 Monitoring

Prometheus scrapes metrics every 15s from `/metrics` and exposes:

- `spam_predictions_total`
- Custom metrics can be added using `prometheus_client`

---

## 📁 File Structure

```
├── app.py                 # Flask app
├── spam_model.pkl         # Trained ML model
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker build instructions
├── docker-compose.yml     # Multi-container orchestration
├── prometheus/
│   └── prometheus.yml     # Prometheus scrape config
├── templates/
│   └── index.html         # Web form UI
├── Jenkinsfile            # CI/CD pipeline script
```

---

## 📹 Demo Video

[📺 Watch the full demo (link here)](https://your-link.com)

---

## 🧠 Author

**Rajat Dulal**  
Deakin University  
Unit: SIT753 – High Distinction Task  
Year: 2025

---

## ✅ License

MIT License – open for educational use.