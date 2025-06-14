# 🚀 Flask App CI/CD Pipeline with GitHub Actions & Google Artifact Registry

---

## 📌 Objective

✅ A simple Python Flask app with a welcome message  
✅ Unit testing setup   
✅ GitHub Actions workflow to automate testing and publish the docker image to Google ArtifactRegistry. 

---

## 🧩 Phase 1: Application Design & Source Code

### 🎯 Requirements

Build a basic Python web application using the Flask framework that displays a welcome message:

> _“Welcome to my learning world”_

### 📂 Folder Structure
<pre>
├── app/│ 
│ └── main.py
├── test/
│ └── test_main.py
├── Dockerfile
├── requirements.txt
└── README.md
</pre>

## 🔁 Phase 2: GitHub Actions CI/CD Pipeline
#### This phase sets up the GitHub Actions workflow to:

- Run unit tests
- If tests pass: build and push Docker image to Google Artifact Registry
- If tests fail: stop the pipeline and log an error
