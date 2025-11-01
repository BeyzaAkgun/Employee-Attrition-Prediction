# Employee Attrition Prediction Web Application

A comprehensive web application that predicts employee attrition using machine learning, featuring a Vue.js frontend, Spring Boot backend, and Flask API for ML services.

## 🚀 Features

- **Employee Attrition Prediction** using AdaBoost Classifier
- **User Authentication** with registration and login
- **File Upload** for CSV and Excel datasets
- **Real-time Analysis** with visual results and pie charts
- **Secure Data Processing** with proper encoding and normalization

## 🏗️ Architecture
Employee-Attrition-Prediction/
├── Vue_Frontend/ # Vue.js frontend application
├── Spring_API/ # Spring Boot backend (authentication)
└── Flask_API/ # Flask API (machine learning services)


## 📊 Machine Learning Performance

- **Accuracy**: 90%
- **F1 Score**: 61%
- **Precision**: 85%
- **Recall**: 48%

## 🛠️ Technology Stack

### Frontend
- Vue.js
- Axios/Fetch for API calls
- Responsive UI Design

### Backend
- Spring Boot (Authentication)
- Flask (Machine Learning API)
- Python (Scikit-learn, Pandas)

### Machine Learning
- AdaBoost Classifier
- Feature Selection (Logistic Regression, Linear SVC, Decision Tree)
- Data Normalization and Encoding

## 📋 Prerequisites

- Node.js (for Vue frontend)
- Java JDK 11+ (for Spring Boot)
- Python 3.8+ (for Flask API)
- MySQL/PostgreSQL (for database)

## 🔧 Installation

### 1. Frontend (Vue.js)
```bash
cd Vue_Frontend
npm install
npm run serve
2. Spring Boot API
bash
cd Spring_API
./mvnw spring-boot:run
3. Flask API
bash
cd Flask_API
pip install -r requirements.txt
python app.py
📁 Project Structure Details
Flask_API/
Machine learning model training and prediction

CSV/Excel file processing

Data normalization and encoding

Spring_API/
User authentication (register/login)

REST API endpoints

Database management

Vue_Frontend/
User interface components

File upload functionality

Results visualization

🎯 Usage
Register/Login to the application

Upload CSV or Excel file with employee data

View attrition prediction results with visual charts

Download analyzed results

📊 Dataset Requirements
The system accepts files with the following attributes:

Age

Monthly Income

Work-Life Balance

Business Travel Frequency

Tenure at Company

[Other features as per model requirements]

👥 Team
Kubilay Kürtür 

Ahmet Yiğit Özkoca 

Beyza Akgün 

İlayda Kasapçopur 


📚 References
IBM HR Analytics Attrition Dataset


