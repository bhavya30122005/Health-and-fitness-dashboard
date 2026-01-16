# health_dashboard.py

import streamlit as st
import pandas as pd
# pip install streamlit pandas

# Load data from CSV file

import plotly.express as px

# Page title
st.title("🏋️ Health and Fitness Dashboard")

# Sidebar for user input
st.sidebar.header("User Info")
name = st.sidebar.text_input("Name", "John Doe")
age = st.sidebar.slider("Age", 10, 80, 30)
height = st.sidebar.number_input("Height (cm)", 140, 220, 170)
weight = st.sidebar.number_input("Weight (kg)", 40, 150, 70)

# BMI calculation
bmi = weight / ((height / 100) ** 2)
st.sidebar.markdown(f"**BMI:** {bmi:.2f}")

# BMI classification
if bmi < 18.5:
    st.sidebar.warning("Underweight")
elif 18.5 <= bmi < 25:
    st.sidebar.success("Normal weight")
elif 25 <= bmi < 30:
    st.sidebar.warning("Overweight")
else:
    st.sidebar.error("Obese")

# Upload fitness CSV data
st.header("📊 Daily Fitness Data")
uploaded_file = st.file_uploader("Upload CSV file with columns: Date, Steps, Calories, SleepHours, HeartRate", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file, parse_dates=["Date"])
    df = df.sort_values("Date")

    st.dataframe(df)

    st.subheader("📈 Activity Over Time")
    col1, col2 = st.columns(2)

    with col1:
        fig_steps = px.line(df, x="Date", y="Steps", title="Steps Over Time")
        st.plotly_chart(fig_steps, use_container_width=True)

    with col2:
        fig_calories = px.line(df, x="Date", y="Calories", title="Calories Burned Over Time")
        st.plotly_chart(fig_calories, use_container_width=True)

    st.subheader("🛌 Sleep & ❤️ Heart Rate")
    col3, col4 = st.columns(2)

    with col3:
        fig_sleep = px.bar(df, x="Date", y="SleepHours", title="Sleep Hours")
        st.plotly_chart(fig_sleep, use_container_width=True)

    with col4:
        fig_hr = px.line(df, x="Date", y="HeartRate", title="Heart Rate")
        st.plotly_chart(fig_hr, use_container_width=True)

else:
    st.info("Please upload your fitness CSV data to view the dashboard.")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
