# 🛡️ Enterprise AI Phishing Detector

A professional-grade, intelligent cybersecurity tool that leverages Machine Learning to identify phishing emails and social engineering attempts based on linguistic patterns.

---

## 🎯 Project Overview

Phishing remains the number one vector for cyber attacks and system breaches. This project provides a predictive security tool designed to protect users by analyzing text payloads for indicators of fraud, artificial urgency, threats, and suspicious links.

### The Solution:
1. **Machine Learning Model:** A predictive classification engine trained on thousands of email indicators.
2. **Web Interface:** A clean, enterprise-ready web application built with Streamlit for local verification of suspicious text payloads.

---

## 💻 Tech Stack

* **Language:** Python 3.x
* **Machine Learning:** Scikit-Learn (Logistic Regression, TF-IDF Vectorization)
* **Data Manipulation:** Pandas
* **Web Framework:** Streamlit
* **Model Serialization:** Joblib

---

## 📁 Project Structure

```text
Phishing_Detector/
│
├── train.py              # Script to train and serialize the ML model
├── app.py                # Streamlit web application interface
├── model.pkl             # Trained Logistic Regression model weights
├── vectorizer.pkl        # Fitted TF-IDF Vectorizer vocabulary
├── requirements.txt      # Project dependencies and libraries
└── phishing_emails.csv   # Dataset used for training and testing