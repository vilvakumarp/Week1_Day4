#Build a BMI calculator (using Ghost text) using Streamlit

import streamlit as st

st.title("BMI Calculator")
st.write("Enter your height and weight to calculate your BMI.")

height = st.number_input("Enter your height (cm):", min_value=0.0, format="%.2f")
weight = st.number_input("Enter your weight (kg):", min_value=0.0, format="%.2f")

if st.button("Calculate BMI"):
    if height > 0 and weight > 0:
        bmi = weight / ((height / 100) ** 2)
        st.success(f"Your BMI is: {bmi:.2f}")
        if bmi < 18.5:
            st.warning("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight.")
        else:
            st.error("You are obese.")
    else:
        st.error("Please enter valid values for height and weight.")