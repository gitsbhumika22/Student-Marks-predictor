# Student Marks Prediction using Machine Learning

An end-to-end Machine Learning project that predicts a student's exam marks based on their study habits and academic performance. The project uses **Linear Regression** to estimate the marks percentage and is deployed as an interactive **Streamlit** web application.


## Live Demo

**Website:** https://your-streamlit-link.streamlit.app


## GitHub Repository

https://github.com/yourusername/Student-Marks-Prediction


## Project Overview

Educational institutions often want to estimate a student's academic performance based on various factors. This project builds a Machine Learning model that predicts the expected marks of a student using historical academic data.

The model is trained using **Supervised Machine Learning (Regression)** and deployed as a user-friendly web application where users can enter student details and instantly receive a predicted marks percentage.


## Problem Statement

Develop a Machine Learning model that predicts a student's marks percentage using the following factors:

- Study Hours
- Attendance Percentage
- Previous Score
- Sleep Hours


## Tech Stack

- Programming Language - Python 
- Data Analysis - Pandas, NumPy 
- Data Visualization - Matplotlib 
- Machine Learning - Scikit-learn 
- Model - Linear Regression 
- Model Saving - Joblib 
- Web Framework - Streamlit 
- Version Control - Git & GitHub 


##  Dataset

Custom dataset

### Input Features

- Study hours
- Attendance percentage
- Previous Score obtained in previous examination
- Sleep Hours


### Target Variable

- Marks obtained


## Machine Learning Workflow

Problem Understanding 
        │
        ▼
Dataset Collection
        │
        ▼
Exploratory Data Analysis (EDA)
        │
        ▼
Data Visualization
        │
        ▼
Data Preprocessing
        │
        ▼
Feature Selection
        │
        ▼
Train-Test Split
        │
        ▼
Linear Regression Model
        │
        ▼
Model Evaluation
        │
        ▼
Save Model (.pkl)
        │
        ▼
Deploy with Streamlit


##  Exploratory Data Analysis (EDA)

The following preprocessing and analysis steps were performed:

- Loaded dataset using Pandas
- Checked dataset shape and structure
- Identified data types
- Checked missing values
- Checked duplicate records
- Generated statistical summary
- Visualized relationships between features
- Selected relevant features for prediction


##  Machine Learning Model

Algorithm Used: Linear Regression

Linear Regression is a supervised learning algorithm used to predict continuous numerical values. Since the output (Marks Percentage) is numerical, this project is a **Regression** problem.


## Model Evaluation

The model was evaluated using the following regression metrics:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

### Model Performance

MAE - 0.45
MSE- 0.35
RMSE - 0.59
$R^2$  - 0.9982


## 📁 Project Structure

```
Student-Marks-Prediction/
│
├── app.py
├── train.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── student_performance.csv
│
├── model/
│   └── student_marks_model.pkl
│
├── notebook/
│   └── Student_Marks_Prediction.ipynb
│
└── assets/
    ├── homepage.png
    └── predicted_score.png
```


##  Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/Student-Marks-Prediction.git
```

### Navigate to the Project Folder

```bash
cd Student-Marks-Prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```



## Future Improvements

- Add more student-related features
- Compare multiple regression algorithms
- Perform hyperparameter tuning
- Improve model performance using ensemble methods
- Deploy using Docker
- Store prediction history in a database
- Build a REST API using Flask or FastAPI


## Key Learnings

Through this project, I learned:

- Supervised Machine Learning
- Regression Problems
- Linear Regression
- Exploratory Data Analysis (EDA)
- Data Preprocessing
- Train-Test Split
- Model Evaluation
- Model Serialization using Joblib
- Streamlit Deployment
- Git & GitHub


## Author

**Bhumika Bhoir**

B.Tech in Information Technology

Aspiring AI/ML Engineer

GitHub: https://github.com/gitsbhumika22

LinkedIn: https://www.linkedin.com/in/bhumika-bhoir-b684a7283

---

⭐ If you found this project useful, consider giving it a star on GitHub!