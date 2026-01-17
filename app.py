import streamlit as st
import pandas as pd
import pickle
import joblib
from sklearn.preprocessing import StandardScaler

label_map = {
    0: "Setosa",
    1: "Versicolor",
    2: "Virginica"
}



def load_model():
    with open("svm_multi.pkl", "rb") as file:
        model = joblib.load("svm_multi.pkl")
    return model


def preprocessing_input_data(data):
    df = pd.DataFrame([data])
    return df


def predict_data(data):
    model = load_model()
    processed_data = preprocessing_input_data(data)
    prediction = model.predict(processed_data)
    return prediction[0]


def main():
    st.title("🌸 Iris Flower Detection")
    st.write("Enter flower measurements to predict the class")

    sl = st.number_input("Sepal Length (cm)", min_value=0.0)
    sw = st.number_input("Sepal Width (cm)", min_value=0.0)
    pl = st.number_input("Petal Length (cm)", min_value=0.0)
    pw = st.number_input("Petal Width (cm)", min_value=0.0)

    if st.button("Predict the class of flower"):
        user_data = {
            'sepal length (cm)': sl,
            'sepal width (cm)': sw,
            'petal length (cm)': pl,
            'petal width (cm)': pw
        }

        prediction = predict_data(user_data)
        flower_name = label_map[prediction]
        st.success(f"🌸 Predicted Flower: {flower_name} ({prediction})")



if __name__ == "__main__":
    main()
