import streamlit as st
import joblib

# Load trained model
model = joblib.load("model/student_marks_model.pkl")

st.set_page_config(
    page_title="Student Marks Prediction",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student Marks Prediction")
st.write("Predict student marks using Machine Learning.")

st.divider()

study_hours = st.number_input(
    "Study Hours",
    min_value=0.0,
    max_value=24.0,
    value=5.0
)

attendance = st.number_input(
    "Attendance Percentage",
    min_value=0.0,
    max_value=100.0,
    value=80.0
)

previous_score = st.number_input(
    "Previous Score",
    min_value=0.0,
    max_value=100.0,
    value=70.0
)

sleep_hours = st.number_input(
    "Sleep Hours",
    min_value=0.0,
    max_value=24.0,
    value=7.0
)

if st.button("Predict Marks"):

    prediction = model.predict([[
        study_hours,
        attendance,
        previous_score,
        sleep_hours
    ]])

    st.success(
        f"Predicted Marks : {prediction[0]:.2f}%"
    )