# 🌸 Iris Flower Classification using SVM

A machine learning web application built with Streamlit that predicts the species of an Iris flower (Setosa, Versicolor, or Virginica) using sepal and petal measurements. The model is trained using a Support Vector Machine (SVM) on the Iris dataset from scikit-learn and provides real-time predictions through a simple and interactive user interface.

## Features
- Multi-class Iris flower classification (0: Setosa, 1: Versicolor, 2: Virginica)
- Streamlit-based interactive web app
- Pre-trained SVM model
- Real-time prediction from user input
- Clean and beginner-friendly structure

## Tech Stack
- Python
- Streamlit
- scikit-learn
- Pandas
- Joblib

## Project Structure
iris-flower-classification-svm/<br>
│<br>
├── app.py                  # Streamlit application for Iris prediction<br>
├── svm_multi.pkl           # Trained SVM multi-class model<br>
├── requirements.txt        # Python dependencies<br>
├── README.md               # Project documentation<br>
│<br>
└── .gitignore              # Files/folders to ignore in Git<br>



## How to Run
1. Clone the repository  
   `git clone https://github.com/your-username/iris-flower-classification-svm.git`
2. Install dependencies  
   `pip install -r requirements.txt`
3. Run the app  
   `streamlit run app.py`

## Input Features
- Sepal Length (cm)
- Sepal Width (cm)
- Petal Length (cm)
- Petal Width (cm)

## Output
- Predicted Iris flower species with label and name

## Author
**Praveen Yadav** – Machine Learning & Python Enthusiast
