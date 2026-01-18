# DevOps Portfolio Project 🚀

A complete **DevOps-focused portfolio application** demonstrating end-to-end development, containerization, and CI/CD automation using **Flask, Docker, Docker Compose, and Jenkins**.

This project is designed especially for **freshers / entry-level DevOps engineers** to showcase real-world practices in application deployment and automation.

---

## 📌 Project Overview

This application is a Flask-based web portfolio that allows users to:

* View a personal DevOps portfolio
* Learn about the tools and technologies used
* Submit comments that are stored persistently

The project demonstrates:

* Backend development using Flask
* Frontend UI with HTML, CSS animations, and JavaScript
* Persistent storage using SQLite
* Containerization with Docker
* Multi-service orchestration using Docker Compose
* CI/CD automation using Jenkins

---


<img width="1919" height="1143" alt="Screenshot 2026-01-18 213914" src="https://github.com/user-attachments/assets/0bf4efc8-04cb-4319-beee-c53c540ebb9a" />


## 🛠️ Tech Stack

### Backend

* Python 3.11
* Flask 3.0
* SQLite (lightweight database)

### Frontend

* HTML5
* CSS3 (custom animations & UI effects)
* JavaScript (AJAX comment submission)

### DevOps Tools

* Docker
* Docker Compose
* Jenkins (CI/CD pipeline)
* Git & GitHub

---

## 📂 Project Structure

```
project/
│── app.py
│── requirements.txt
│── Dockerfile
│── docker-compose.yml
│── Jenkinsfile
│── comments.db
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    ├── script.js
    └── images/
        └── profile.jpg
```

---

## ⚙️ Application Workflow

1. User accesses the web application
2. Frontend UI is rendered using HTML & CSS
3. User submits a comment via the form
4. Flask backend processes the request
5. Comment is stored in SQLite database
6. Updated comments are displayed on the UI

---

## 🐳 Docker Workflow

### Build Docker Image

```bash
docker build -t devops-portfolio .
```

### Run Container

```bash
docker run -p 5000:5000 devops-portfolio
```

---

## 🧩 Docker Compose

Docker Compose is used to:

* Manage application lifecycle
* Persist database data using volumes
* Simplify deployment

### Run with Docker Compose

```bash
docker compose up -d
```

---

## 🔁 Jenkins CI/CD Pipeline

The Jenkins pipeline performs:

1. Code checkout from GitHub
2. Docker image build
3. Smoke testing inside container
4. Deployment using Docker Compose
5. Automatic cleanup

### Jenkins Stages

* Checkout
* Build Docker Image
* Smoke Test
* Deploy
<img width="1914" height="1090" alt="Screenshot 2026-01-18 213421" src="https://github.com/user-attachments/assets/223179e4-8eae-4e93-87b7-79472e067e98" />

---

## 📈 DevOps Best Practices Followed

* Containerized application
* Persistent data storage
* CI/CD automation
* Environment isolation
* Clean and reproducible builds
* Production-ready project structure

---

## 🎯 Why This Project Matters

This project simulates a **real DevOps workflow** and can be confidently showcased in:

* Job interviews
* GitHub portfolio
* Resume projects

It demonstrates not just coding skills, but also **deployment, automation, and operational thinking**.

---
Final Output :
we can Expose this by using localhost:5000


<img width="1905" height="1086" alt="Screenshot 2026-01-18 213449" src="https://github.com/user-attachments/assets/ad7144c7-6dff-4174-9491-d4c67bf8cb2b" />




---

## 👤 Author

**Vamsi Kandula**
Aspiring DevOps Engineer

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to fork or extend it.

Happy Learning & Happy DevOps! 🔥
